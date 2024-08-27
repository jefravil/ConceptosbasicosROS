#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


def callback(msg): 
  print ("velocidad linealX %.2f"%msg.linear.x)
  print ("velocidad angular %.2f"% msg.angular.z)
  #val= Twist()
  #val= Twist.angular.z

if __name__ == "__main__":
    rospy.init_node('cmdVel_subscriber')
    sub = rospy.Subscriber('/cmd_vel', Twist, callback)
    rospy.spin()