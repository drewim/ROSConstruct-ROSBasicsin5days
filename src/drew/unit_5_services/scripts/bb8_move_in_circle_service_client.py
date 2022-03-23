#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node("service_client")

rospy.wait_for_service('/move_bb8_in_circle')
bb8_move_in_circle_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
bb8_move_in_circle_object = EmptyRequest()
bb8_move_in_circle_service(bb8_move_in_circle_object)
rospy.spin()
