#! /usr/bin/env python

"""
#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse # you import the service message python classes  # generated from MyCustomServiceMessage.srv.
from geometry_msgs.msg import Twist
import time

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
    
    print("Request Data==> duration="+str(request.duration))
    my_response = MyCustomServiceMessageResponse()
    if request.duration > 0:
        controlBB8(1,1,request.duration)
        my_response.success = True

    else:
        my_response.success = False
    return  my_response # the service Response class, in this case MyCustomServiceMessageResponse

rospy.init_node('service_movebb8custom_server') 
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
pub= rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.spin() # maintain the service open.

"""
#! /usr/bin/env python

import rospy
#from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse # you import the service message python classes  # generated from MyCustomServiceMessage.srv.
from my_custom_srv_msg_pkg.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist
import time

speed = 0.2 # m/s
turn = 1

def sqBB8(side,repetitions):
    for __ in range(repetitions):
        for _ in range(4):
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = 0
            pub.publish(twist)
            tiempo=side*5 #como nuestra vel es 0.2 m/s necesitamos multiplicar
            #por 5 para que en 5 seg se mueva 1 m
            rospy.sleep(tiempo)
            twist.linear.x = 0
            twist.angular.z = 1.5707963267948966 #1.57rad/s
            pub.publish(twist)
            rospy.sleep(1) #1seg para que gire 90 deg que son 1.57 rad
            twist.linear.x = 0
            twist.angular.z = 0
            pub.publish(twist)

def my_callback(request):
    #request tiene los parametros que necesitamos
    #estos parametros se definienron en el .srv
    my_response = BB8CustomServiceMessageResponse()
    #my ressponse tiene en cambio el parametro de la repuesta
    if request:

        sqBB8(request.side,request.repetitions)

        my_response.success = True

    else:
        my_response.success = False
    return  my_response # the service Response class, in this case MyCustomServiceMessageResponse

rospy.init_node('service_movebb8custom_server') 
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
pub= rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.spin() # maintain the service open.
