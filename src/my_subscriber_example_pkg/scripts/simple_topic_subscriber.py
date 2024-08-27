#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32 

def callback(msg): 
  print (msg.pose.pose)
  print (msg.pos.pose)
  print (msg.pose.pose)
  print (msg.)


rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('/counter', Int32, callback)
rospy.spin()