#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist


def my_callback(request):
    #print("my_callback has been called")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
    move = Twist()
    move.linear.x = -0.6
    move.angular.z = -0.8
    pub.publish(move)
    return EmptyResponse()


rospy.init_node('bb8_move_in_circle')

bb8_move_service = rospy.Service('/move_bb8_in_circle', Empty, my_callback)
rospy.spin()  # maintain the service open.
