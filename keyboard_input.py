#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
import sys

twist = Twist()

def keyboard_input ():

	pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	rospy.init_node('keyboard_input')
	
	
	print("Let's move the robot!")
	speed = input("Enter your speed:") #custom speed val
	turn = input ("Enter turn value: ") #custom turn val
	
	
	
	while not rospy.is_shutdown():
		s = input(":- ")
		if s == "w":
			twist.linear.x = 1*int(speed)
			twist.angular.z = 0
			twist.linear.y = 0
		elif s == "s":
			twist.linear.x = -1*int(speed)
			twist.angular.z = 0
			twist.linear.y = 0
		elif s == "d":
			twist.linear.y = -1*int(speed)
			twist.angular.z = 0
			twist.linear.x = 0
		elif s == "a":
			twist.linear.y = 1*int(speed)
			twist.angular.z = 0
			twist.linear.x = 0
		elif s == "k":
			twist.angular.z = 2*int(speed)
			twist.linear.x = twist.linear.y = 0
		elif s == "l":
			twist.angular.z = -2*int(speed)
			twist.linear.x = twist.linear.y = 0
		elif s == "q":
			twist.angular.z = twist.linear.x = twist.linear.y = 0
			sys.exit()
		pub.publish(twist)
		
	
	
if __name__ == '__main__':
    try:
        keyboard_input()
    except rospy.ROSInterruptException:pass
