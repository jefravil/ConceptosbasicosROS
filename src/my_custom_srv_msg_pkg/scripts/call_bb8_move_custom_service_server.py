#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest# you import the service message python classes  # generated from MyCustomServiceMessage.srv.
from geometry_msgs.msg import Twist

rospy.init_node('service_movebb8custom_client')
rospy.wait_for_service('/move_bb8_in_circle_custom')
serviceConectionObject= rospy.ServiceProxy('/move_bb8_in_circle_custom',MyCustomServiceMessage)

serviceRequestObject= MyCustomServiceMessageRequest()
serviceRequestObject.duration=8
result= serviceConectionObject(serviceRequestObject)
print(result)

