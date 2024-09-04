#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import BB8CustomServiceMessage,BB8CustomServiceMessageRequest # you import the service message python classes  # generated from MyCustomServiceMessage.srv.


rospy.init_node('service_movebb8custom_client')
rospy.wait_for_service('/move_bb8_in_square_custom')
serviceConectionObject= rospy.ServiceProxy('/move_bb8_in_square_custom',BB8CustomServiceMessage)

serviceRequestObject= BB8CustomServiceMessageRequest()
serviceRequestObject.side=1
serviceRequestObject.repetitions=2
result= serviceConectionObject(serviceRequestObject)
print(result)
serviceRequestObject.side=2
serviceRequestObject.repetitions=1
result= serviceConectionObject(serviceRequestObject)
print(result)
