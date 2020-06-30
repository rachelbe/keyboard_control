#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
import sys
import getch

twist = Twist()

def keyboard_input ():

	pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	rospy.init_node('keyboard_input')
	
	print("Let's move the robot!")
	speed = input("Enter speed:") #custom speed val
	turn = input ("Enter turn value: ") #custom turn val
	
	while not rospy.is_shutdown():
		
		
		s =getch.getch()  #input to move 
		if s == "w": #foward
			twist.linear.x = -1*int(speed) 
			twist.angular.z = 0
			twist.linear.y = 0
		elif s == "s":  #backward
			twist.linear.x = 1*int(speed)
			twist.angular.z = 0
			twist.linear.y = 0
		elif s == "q": #foward and right
			twist.linear.y = -1*int(speed)
			twist.angular.z = -1*int(turn)
			twist.linear.x = -1*int(speed)
		elif s == "e": #foward and left
			twist.linear.y = 1*int(speed)
			twist.angular.z = 1*int(turn)
			twist.linear.x = -1*int(speed)
		elif s == "a": #backwards and right
			twist.linear.y = -1*int(speed)
			twist.angular.z = -1*int(turn)
			twist.linear.x = 1*int(speed)
		elif s == "d": #backwards and left
			twist.linear.y = 1*int(speed)
			twist.angular.z = 1*int(turn)
			twist.linear.x = 1*int(speed)	
		elif s == "k": #turn around right
			twist.angular.z = 2*int(speed)
			twist.linear.x = twist.linear.y = 0
		elif s == "l": #turn around left
			twist.angular.z = -2*int(turn)
			twist.linear.x = twist.linear.y = 0
		elif s == "z": #quit
			twist.angular.z = twist.linear.x = twist.linear.y = 0
			sys.exit()
		pub.publish(twist)
		
	
if __name__ == '__main__':
    try:
        keyboard_input()
    except rospy.ROSInterruptException:pass
