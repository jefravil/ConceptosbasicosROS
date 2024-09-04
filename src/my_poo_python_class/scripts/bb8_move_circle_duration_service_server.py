#! /usr/bin/env python

import rospy
#from std_srvs.srv import Empty, EmptyResponse 
from bb8_move_circle_duration_class import MoveBB8
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    movebb8_object = MoveBB8()
    movebb8_object.move_bb8(duration=request.duration)
    rospy.loginfo("Finished service move_bb8_in_circle")
    result= MyCustomServiceMessageResponse()
    result.success= True
    return result

rospy.init_node('service_move_duration_bb8_in_circle_server') 
my_service = rospy.Service('/move_bb8_duration_in_circle', MyCustomServiceMessage , my_callback)
rospy.loginfo("Service /move_bb8_in_circle Ready")
rospy.spin() # keep the service open.