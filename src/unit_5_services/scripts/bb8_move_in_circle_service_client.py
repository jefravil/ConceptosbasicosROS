#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty , EmptyRequest

rospy.init_node('bb8_circle_service_client')
rospy.wait_for_service('/move_bb8_in_circle')
serviceConectionObject= rospy.ServiceProxy('/move_bb8_in_circle',Empty)

serviceRequestObject= EmptyRequest()
result= serviceConectionObject(serviceRequestObject)
print(result)

