#! /usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
import time
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.

speed = .2
turn = 1

def controlBB8(linearX=0.0, angular=0.0, duration=0):
    twist = Twist()
    twist.linear.x = speed*linearX
    twist.angular.z = turn*angular
    pub.publish(twist)
    time.sleep(duration) #este time sleep no me gusta pero bueno
    twist.linear.x = 0
    twist.angular.z = 0
    pub.publish(twist)

def my_callback(request):
    print("My_callback has been called")
    print("Moviendo BB8")
    controlBB8(1,1,6.28)
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 
    

    

rospy.init_node('move_bb8_service_server') 
my_service = rospy.Service('/move_bb8_in_circle', Empty, my_callback) # create the Service called my_service with the defined callback
pub= rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.spin() # maintain the service open.
