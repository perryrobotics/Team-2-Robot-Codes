#!/usr/bin/python
import os, sys
from wallaby import *

LEFT_LINE_SENSOR = 3
RIGHT_LINE_SENSOR = 2
THRESH = 2300

def drive_straight(speed, dist_to_go):
	set_create_distance(0)
  	create_drive_direct(speed, speed)
  	while get_create_distance() < dist_to_go:
		#print get_create_distance(), ":", dist_to_go
		#pass
		msleep(10)
 	create_drive_direct(0,0)
 
def drive_backwards(speed, dist_to_go):
	set_create_distance(0)
  	create_drive_direct(-speed, -speed)
  	while get_create_distance() > -dist_to_go:
		#pass
		msleep(10)
 	create_drive_direct(0,0)
            
def spin_CCW(speed, angle_to_go):
	set_create_total_angle(0)
  	create_spin_CCW(speed)
  	while get_create_total_angle() < angle_to_go:
		#pass
		msleep(10)
 	create_drive_direct(0,0)
            
def spin_CW(speed, angle_to_go):
	set_create_total_angle(0)
  	create_spin_CW(speed)
  	while get_create_total_angle() > -angle_to_go:
		#pass
		msleep(10)
 	create_drive_direct(0,0)
            
def drive_till_bump(speed):
	create_drive_direct(speed, speed)
  	while get_create_lbump() == 0 and get_create_rbump()==0:
		#pass
		msleep(10)
 	create_drive_direct(0,0)
        
def back_till_bump(speed):
	create_drive_direct(-speed, -speed)
  	while get_create_lbump() == 0 and get_create_rbump()==0:
		#pass
		msleep(10)
 	create_drive_direct(0,0)
            
def drive_until_black(speed):
	create_drive_direct(speed, speed)
	while analog(LEFT_LINE_SENSOR) < THRESH:
		pass
	create_drive_direct(0,0)
            
def drive_backwards_until_black(speed):
	create_drive_direct(-speed, -speed)
	while analog(LEFT_LINE_SENSOR) < THRESH:
		pass
	create_drive_direct(0,0)
     
def spin_CCW_to_black(speed):
	create_spin_CCW(speed)
	while analog(RIGHT_LINE_SENSOR) < THRESH:
		pass
	create_drive_direct(0,0)
            
def spin_CW_to_black(speed):
	create_spin_CW(speed)
	while analog(RIGHT_LINE_SENSOR) < THRESH:
		pass
	create_drive_direct(0,0)
            
            
def follow_line(speed, dist_to_go):
	set_create_distance(0)

  	while get_create_distance() > -dist_to_go:
		if analog(LEFT_LINE_SENSOR) > THRESH:
			spin_CW(speed/3, 3)
			create_drive_direct(-speed, -speed )
		elif analog(RIGHT_LINE_SENSOR) > THRESH:
			spin_CCW(speed/3, 3)
			create_drive_direct(-speed, -speed)
		else:
			create_drive_direct(-speed, -speed)
	create_drive_direct(0,0)

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            