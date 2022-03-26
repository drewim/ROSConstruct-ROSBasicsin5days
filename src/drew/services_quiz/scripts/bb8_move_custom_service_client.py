#! /usr/bin/env python

#import random
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('service_client')

for i in range(2):
    # Wait for service to start
    rospy.wait_for_service('/move_bb8_in_square_custom')
    move_bb8_custom_service = rospy.ServiceProxy(
        '/move_bb8_in_square_custom', BB8CustomServiceMessage)  # create connection to the service
    # create an object of type BB8CustomServiceMessageRequest
    move_bb8_custom_object = BB8CustomServiceMessageRequest()
    # fill the object with the size and repetitions for the square move
    if i == 0:
        move_bb8_custom_object.side = 2.0
        move_bb8_custom_object.repetitions = 2
    elif i == 1:
        move_bb8_custom_object.side = 4.0
        move_bb8_custom_object.repetitions = 1
    # send through the connection the duration of the bb8 move
    result = move_bb8_custom_service(move_bb8_custom_object)
    print(result)
