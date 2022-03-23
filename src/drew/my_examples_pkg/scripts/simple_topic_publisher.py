#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
#count = Int32()
#count.data = 0
speed = Twist()
speed.linear.x = .8
#speed.linear.y = 0
speed.angular.z = .5

while not rospy.is_shutdown():
    pub.publish(speed)
    # print(speed_linear)
    #count.data += 1
    rate.sleep()
