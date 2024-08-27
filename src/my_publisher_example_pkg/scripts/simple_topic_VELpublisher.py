#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import random

speed = .2
turn = 1


def cambiomov(linearX=0.0,angularZ=0.0):
            twist = Twist()
            twist.linear.x = linearX*speed
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = angularZ*turn
            pub.publish(twist)

if __name__=="__main__":

    try:
        rospy.init_node('cmdvel_topic_publisher')
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        count=0
        rate = rospy.Rate(2)
        while not rospy.is_shutdown() and count!=100:
            

            x = random.choice([-1, 1 , 0])
            th = random.choice([-1, 1, 0])
            cambiomov(x,th)
            count+=1   
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
    finally:
        cambiomov(0,0)


