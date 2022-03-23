#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32
from my_examples_pkg.msg import Age

rospy.init_node('age_publisher')
pub = rospy.Publisher('/age', Age, queue_size=1)
rate = rospy.Rate(2)
age = Age()
age.years = 1
age.months = 2
age.days = 3

while not rospy.is_shutdown():
    pub.publish(age)
    rate.sleep()
