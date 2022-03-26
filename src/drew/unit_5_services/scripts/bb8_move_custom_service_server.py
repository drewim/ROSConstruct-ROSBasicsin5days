#! /usr/bin/env python

import time
import rospy
# you import the service message python classes
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from geometry_msgs.msg import Twist


def my_callback(request):
    print("Request Data==> duration="+str(request.duration))
    my_response = MyCustomServiceMessageResponse()
    bb8_move(request.duration)
    if request.duration > 5.0:
        my_response.success = True
    else:
        my_response.success = False
    # the service Response class, in this case MyCustomServiceMessageResponse
    return my_response


def bb8_move(duration):
    timer = time.time()
    move = Twist()
    while (time.time()-timer) < duration:
        move.linear.x = -0.6
        move.angular.z = -0.8
        pub.publish(move)
    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)


rospy.init_node('service_client')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
bb8_move_service = rospy.Service(
    '/move_bb8_in_circle_custom', MyCustomServiceMessage, my_callback)
rospy.spin()  # maintain the service open.
