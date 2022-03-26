#! /usr/bin/env python

import time
import rospy
# you import the service message python classes
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist


def my_callback(request):
    print("Request Data==> side="+str(request.side))
    print("Request Data==> repetitions="+str(request.repetitions))
    my_response = BB8CustomServiceMessageResponse()
    reps = bb8_move(request.side, request.repetitions)
    if request.repetitions == reps:
        my_response.success = True
    else:
        my_response.success = False
    # the service Response class, in this case MyCustomServiceMessageResponse
    return my_response


def bb8_move(side, repetitions):
    move = Twist()
    base_speed = 1  # speed to run robot. Multiply by side to get move speed
    move.angular.z = 0
    for i in range(repetitions):
        for x in range(4):
            move.linear.x = base_speed
            move.angular.z = 0
            pub.publish(move)
            time.sleep(side)
            move.linear.x = .1
            move.angular.z = 1
            pub.publish(move)
            time.sleep(2.25)
    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)
    return i+1


rospy.init_node('service_server')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
bb8_move_service = rospy.Service(
    '/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback)
rospy.spin()  # maintain the service open.
