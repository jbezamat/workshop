#!/usr/bin/env python
import rospy
from gpiozero import Button
from workshop.msg import Bumpers

def bumper():
    rospy.init_node('bumper', anonymous=True)
    pub = rospy.Publisher('bumper_topic', Bumpers, queue_size=10)
    rate = rospy.Rate(10) # 10hz


    bumpers = Bumpers()
    button_left = Button(24, pull_up=True)
    button_right = Button(23, pull_up=True)
    while not rospy.is_shutdown():
        bumpers.BUMPER_LEFT = button_left.is_pressed
        bumpers.BUMPER_RIGHT = button_right.is_pressed
        #msg_str = "%s %s" % bumpers.BUMPER_LEFT, bumpers.BUMPER_RIGHT
        #rospy.loginfo(msg_str)
        pub.publish(bumpers)
        rate.sleep()

if __name__ == '__main__':
    try:
        bumper()
    except rospy.ROSInterruptException:
        pass