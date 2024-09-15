#! /usr/bin/env python
import rospy

import actionlib
#Test tiene los 3 parametros como int32
#ojo segun Chat pero probando me dio los mismos resultados
''' 
¿Son lo mismo TestResult y TestActionResult?
No, TestResult y TestActionResult no son lo mismo, aunque están relacionados.
'''
#from actionlib.msg import TestAction ,TestActionFeedback, TestActionResult
from actionlib.msg import TestAction ,TestFeedback, TestResult
#from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class ArdroneSquareClass(object):
    
  # create messages that are used to publish feedback/result
  _feedback = TestFeedback()
  _result   = TestResult()
  lado = 0
    
  def __init__(self):
    # creates the action server
    
    self._as = actionlib.SimpleActionServer("ArdroneSquareClass", TestAction, self.goal_callback, False)
    self._as.start()
    self.move_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    self.takeoff_pub = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
    self.land_pub = rospy.Publisher('/drone/land', Empty, queue_size=1)
    self.move_msg = Twist()
    self.takeoff_msg = Empty()
    self.land_msg = Empty()
    self.rate = rospy.Rate(10)


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

  def takeoff(self, duration=3):
        while self.takeoff_pub.get_num_connections()<1:
            rospy.loginfo('Waiting for drone takeoff')
        rospy.loginfo('Taking off...')
        for _ in range(duration):
            self.takeoff_pub.publish(self.takeoff_msg)
            rospy.sleep(1)
  
  def land(self, duration=3):
        while self.land_pub.get_num_connections()<1:
            rospy.loginfo('Waiting for drone landing')
        rospy.loginfo('Landing...')
        for _ in range(duration):
            self.move_msg.linear.x = 0
            self.move_msg.angular.z = 0
            self.move_pub.publish(self.move_msg)
            self.land_pub.publish(self.land_msg)
            rospy.sleep(1)  
    
  def goal_callback(self, goal):
    # this callback is called when the action server is called.
    # this is the function that computes the Fibonacci sequence
    # and returns the sequence to the node that called the action server
    
    # helper variables
    #r = rospy.Rate(1)
    success = True
    self.lado= goal.goal
    # append the seeds for the fibonacci sequence
    self._feedback.feedback =0
    # publish info to the console for the user
    #rospy.loginfo('"fibonacci_as": Executing, creating fibonacci sequence of order %i with seeds %i, %i' % ( goal.order, self._feedback.sequence[0], self._feedback.sequence[1]))
    rospy.loginfo('"ardroneSquare_as": Executing, moviendo una distancia de %i' % ( goal.goal))
    
    
    self.takeoff()
    start_time = rospy.get_time()

    for i in range(1, 5):
    
      # check that preempt (cancelation) has not been requested by the action client
      if self._as.is_preempt_requested():
        rospy.loginfo('The goal has been cancelled/preempted')
        # the following line, sets the client in preempted state (goal cancelled)
        self._as.set_preempted()
        success = False
        # we end the calculation of the Fibonacci sequence
        break
    
      
      # builds the next feedback msg to be sent
      #self._feedback.sequence.append(self._feedback.sequence[i] + self._feedback.sequence[i-1])
      # publish the feedback
      #self._as.publish_feedback(self._feedback)
      
      self.move_forward_drone(self.lado)
      self.turn_drone()
      self._feedback.feedback = i
      self._as.publish_feedback(self._feedback)
      # the sequence is computed at 1 Hz frequency
      self.rate.sleep()
    
    self.land()
    end_time = rospy.get_time()
    total_time = end_time - start_time
    # at this point, either the goal has been achieved (success==true)
    # or the client preempted the goal (success==false)
    # If success, then we publish the final result
    # If not success, we do not publish anything in the result
    if success:
      self._result.result =int(total_time) 
      rospy.loginfo('Succeeded moving the drone')
      self._as.set_succeeded(self._result)
      
if __name__ == '__main__':
  rospy.init_node('ardroneSquareClass')
  ArdroneSquareClass()
  rospy.spin()