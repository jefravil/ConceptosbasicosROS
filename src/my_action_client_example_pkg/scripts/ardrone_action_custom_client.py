#! /usr/bin/env python
import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
import random

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
def feedback_callback(feedback):
    """
    Error that might jump
    
    self._feedback.lastImage = 
AttributeError: 'ArdroneAS' obj
    
    """
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

# We create some constants with the corresponing vaules from the SimpleGoalState class
PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

nImage = 1

speed = 0.5
turn = 1


def movientoArdrone(pub,orden):
    twist= Twist()
    if (orden==1):
        x = random.choice([-1, 0, 1])
        th = random.choice([-1, 0, 1])
        twist.linear.x= speed*x
        twist.angular.z= turn*th
        pub.publish(twist)
        #rospy.sleep(1) 
    elif(orden==0):
        twist.linear.x= 0
        twist.angular.z= 0
        pub.publish(twist)


# initializes the action client node
rospy.init_node('example_no_waitforresult_action_client_node')

#Despegue
#rostopic pub /drone/takeoff std_msgs/Empty "{}"
despegarPub= rospy.Publisher('/drone/takeoff',Empty,queue_size=1)
while despegarPub.get_num_connections()<1:
    rospy.loginfo('Waiting for drone takeoff')
#Aterrizaje
aterrizajePub= rospy.Publisher('/drone/land',Empty,queue_size=1)

msjVacio= Empty()
despegarPub.publish(msjVacio)
rospy.sleep(1)

#Movimiento
CmdPub= rospy.Publisher('/cmd_vel', Twist, queue_size=1)

#Action client
action_server_name = '/ardrone_action_server'
client = actionlib.SimpleActionClient(action_server_name, ArdroneAction)

# waits until the action server is up and running
rospy.loginfo('Waiting for action Server '+action_server_name)
client.wait_for_server()
rospy.loginfo('Action Server Found...'+action_server_name)

# creates a goal to send to the action server
goal = ArdroneGoal()
goal.nseconds = 10 # indicates, take pictures along 10 seconds

client.send_goal(goal, feedback_cb=feedback_callback)


# You can access the SimpleAction Variable "simple_state", that will be 1 if active, and 2 when finished.
#Its a variable, better use a function like get_state.
#state = client.simple_state
# state_result will give the FINAL STATE. Will be 1 when Active, and 2 if NO ERROR, 3 If Any Warning, and 3 if ERROR
state_result = client.get_state()

rate = rospy.Rate(1)

rospy.loginfo("state_result: "+str(state_result))

while state_result < DONE:
    rospy.loginfo("Doing move while waiting for the Server to give a result....")
    movientoArdrone(CmdPub,1)
    rate.sleep()
    state_result = client.get_state()
    rospy.loginfo("state_result: "+str(state_result))

#DETENIENDO MOVIMIENTO 
rospy.loginfo("[Result] State: "+str(state_result))
rospy.loginfo("Stoping Movement")
movientoArdrone(CmdPub,0)
aterrizajePub.publish(msjVacio)

if state_result == ERROR:
    rospy.logerr("Something went wrong in the Server Side")
if state_result == WARN:
    rospy.logwarn("There is a warning in the Server Side")

#rospy.loginfo("[Result] State: "+str(client.get_result()))