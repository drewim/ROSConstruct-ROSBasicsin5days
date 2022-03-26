#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

class MoveBB8():

    def __init__(self):
        self.bb8_vel_publisher = rospy.Publisher(
            '/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        self.rate = rospy.Rate(10)  # 10hz
        self.move_bb8_service=rospy.ServiceProxy('/move_bb8_in_circle', MyCustomServiceMessage)
        self.move_bb8_object=MyCustomServiceMessageRequest()
        rospy.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuous publishing systems, this is no big deal, but in systems that publish only
        once, it IS very important.
        """
        while not self.ctrl_c:
            connections = self.bb8_vel_publisher.get_num_connections()
            if connections > 0:
                self.bb8_vel_publisher.publish(self.cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()

    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True

    def move_bb8(self, duration, linear_speed=0.2, angular_speed=0.2):

        self.cmd.linear.x = linear_speed
        self.cmd.angular.z = angular_speed

        rospy.loginfo("Moving BB8!")
        self.publish_once_in_cmd_vel()
        
        rospy.sleep(duration)
        self.cmd.linear.x = 0
        self.cmd.angular.z = 0
        self.publish_once_in_cmd_vel()
    
    #def call_move_bb8_service(self, time):
    #    rospy.wait_for_service('/move_bb8_in_circle')
    #    self.move_bb8_object.duration = time
    #    result = self.move_bb8_service(self.move_bb8_object)
        
        


if __name__ == '__main__':
    rospy.init_node('move_bb8_test', anonymous=True)
    movebb8_object = MoveBB8()
    move_time=4
    try:
        movebb8_object.move_bb8(move_time)
    except rospy.ROSInterruptException:
        pass
