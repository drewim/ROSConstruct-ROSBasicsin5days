#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32
from nav_msgs.msg import Odometry


def callback(msg):
    print(msg.twist.twist.linear.x)


rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()
