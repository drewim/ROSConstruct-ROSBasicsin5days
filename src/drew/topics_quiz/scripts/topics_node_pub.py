#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node('topics_quiz_node')  # init node as required by quiz


def messageSub():
    # Subscribe to Laser Scan topic, and print its values to messagePub function
    sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, messagePub)


def messagePub(msg):
    # Will publish values to /cmd_vel depending on values read from laserscan
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    scan_array = msg.ranges  # creates array to take in laserscan ranges
    command = checkScan(scan_array)
    speed = Twist()  # Twist is message to /cmd_vel topic
    if command == "fwd":
        speed.linear.x = 0.5
        speed.angular.z = 0
        pub.publish(speed)
    elif command == "right":
        speed.linear.x = 0
        speed.angular.z = -0.5
        pub.publish(speed)
    elif command == "left":
        speed.linear.x = 0
        speed.angular.z = 0.5
        pub.publish(speed)

    # while not rospy.is_shutdown():


def checkScan(array):
    length = len(array)
    # pull out middle 1/3 of array
    center = array[int(length/3):int(length*(2/3))]
    right = array[int(length*(2/3))::]
    left = array[::int(length*(1/3))]
    # print(right)
    thresh = 1  # min distance required from wall
    # if statements based on center values of scan
    if all(x > thresh for x in center):
        return "fwd"
    elif any(x < thresh for x in center):
        return "left"
    # if statements to control turning if values less than thresh
    if any(x < thresh for x in right):
        return "left"
    if any(x < thresh for x in left):
        return "right"


if __name__ == '__main__':
    rate = rospy.Rate(2)
    try:
        messageSub()
        # messagePub()
    except rospy.ROSInterruptException:
        pass
    rate.sleep()
    rospy.spin()
