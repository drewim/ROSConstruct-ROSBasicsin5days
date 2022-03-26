#! /usr/bin/env python

import random
import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node('service_server_call')

# Wait for service to start
rospy.wait_for_service('/move_bb8_in_circle_custom')
move_bb8_custom_service = rospy.ServiceProxy(
    '/move_bb8_in_circle_custom', MyCustomServiceMessage)  # create connection to the service
# create an object of type MyCustomServiceMessageRequest
move_bb8_custom_object = MyCustomServiceMessageRequest()
# rand int from 5-12 for duration of move of service
dur = random.randint(5, 12)
# fill the duration of the object with the random time created
move_bb8_custom_object.duration = dur
# send through the connection the duration of the bb8 move
result = move_bb8_custom_service(move_bb8_custom_object)
print(result)
