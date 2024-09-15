#! /usr/bin/env python
import rospy

import actionlib
#Test tiene los 3 parametros como int32

#from actionlib.msg import TestAction ,TestActionFeedback, TestActionResult
from actions_quiz.msg import CustomActionMsgAction, CustomActionMsgResult, CustomActionMsgFeedback
#from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty


class ArdroneSquareClass(object):
    
  # create messages that are used to publish feedback/result
  _feedback = CustomActionMsgFeedback()
  _result   = CustomActionMsgResult()
  lado = 0
    
  def __init__(self):
    # creates the action server
    
    self._as = actionlib.SimpleActionServer("action_custom_msg_as", CustomActionMsgAction, self.goal_callback, False)
    self._as.start()
    self.move_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    self.takeoff_pub = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
    self.land_pub = rospy.Publisher('/drone/land', Empty, queue_size=1)
    self.move_msg = Twist()
    self.takeoff_msg = Empty()
    self.land_msg = Empty()
    self.rate = rospy.Rate(1)


  def move_forward_drone(self,lado):
        self.move_msg.linear.x = 1 #m/s
        self.move_pub.publish(self.move_msg)
        rospy.loginfo('Moving forward...')
        rospy.sleep(lado)
        self.move_msg.linear.x = 0 #m/s
        self.move_pub.publish(self.move_msg)

  def turn_drone(self):
        self.move_msg.angular.z = 1.60 #rad/s
        self.move_pub.publish(self.move_msg)
        rospy.loginfo('turnning...')
        rospy.sleep(1)
        self.move_msg.angular.z = 0 #rad/s
        self.move_pub.publish(self.move_msg)

  def takeoff(self):
        while self.takeoff_pub.get_num_connections()<1:
            rospy.loginfo('Waiting for drone takeoff')
        rospy.loginfo('Taking off...')
        
        self.takeoff_pub.publish(self.takeoff_msg)
            
  
  def land(self):
        while self.land_pub.get_num_connections()<1:
            rospy.loginfo('Waiting for drone landing')
        rospy.loginfo('Landing...') 

        self.land_pub.publish(self.land_msg)
              
    
  def goal_callback(self, goal):
    # this callback is called when the action server is called.
    # this is the function that computes the Fibonacci sequence
    # and returns the sequence to the node that called the action server
    success = True
    
    self.ordenDespegueAterrizaje= goal.goal
    
    rospy.loginfo('"action_custom_msg_as": Ejecutando la orden: ' + str( goal.goal))
    
    for i in range(3):
        if (self.ordenDespegueAterrizaje=='TAKEOFF'):
            self.takeoff()
            # the sequence is computed at 1 Hz frequency
            #self.rate.sleep()
        elif (self.ordenDespegueAterrizaje=='LAND'):
            self.land()
            # the sequence is computed at 1 Hz frequency
            #self.rate.sleep()
        else:
            success = False
        self._feedback.feedback = self.ordenDespegueAterrizaje
        self._as.publish_feedback(self._feedback)
        self.rate.sleep()
    
    if success:
      rospy.loginfo('Succeeded moving the drone')
      self._as.set_succeeded()
    
    # at this point, either the goal has been achieved (success==true)
    # or the client preempted the goal (success==false)
    # If success, then we publish the final result
    # If not success, we do not publish anything in the result
    
      
if __name__ == '__main__':
  rospy.init_node('ardroneSquareClass')
  ArdroneSquareClass()
  rospy.spin()