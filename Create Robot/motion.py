#!/usr/bin/python
import os, sys
from wallaby import *

def drive_straight(speed, dist_to_go):
	set_create_distance(0)
  	create_drive_direct(speed, speed)
  	while get_create_distance() < dist_to_go:
		print get_create_distance(), ":", dist_to_go
		pass
 	create_drive_direct(0,0)
 
def drive_backwards(speed, dist_to_go):
	set_create_distance(0)
  	create_drive_direct(-speed, -speed)
  	while get_create_distance() > -dist_to_go:
		pass
 	create_drive_direct(0,0)
            
def spin_CCW(speed, angle_to_go):
	set_create_total_angle(0)
  	create_spin_CCW(speed)
  	while get_create_total_angle() < angle_to_go:
		pass
 	create_drive_direct(0,0)
            
def spin_CW(speed, angle_to_go):
	set_create_total_angle(0)
  	create_spin_CW(speed)
  	while get_create_total_angle() > -angle_to_go:
		pass
 	create_drive_direct(0,0)
            
def drive_till_bump(speed):
	create_drive_direct(speed, speed)
  	while get_create_lbump() == 0 and get_create_rbump()==0:
		pass
 	create_drive_direct(0,0)
        
def back_till_bump(speed):
	create_drive_direct(-speed, -speed)
  	while get_create_lbump() == 0 and get_create_rbump()==0:
		pass
 	create_drive_direct(0,0)
            
      
