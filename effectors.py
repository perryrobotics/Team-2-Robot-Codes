#!/usr/bin/python
import os, sys
from wallaby import *

ARM = 3
ARM_SU = 450
ARM_UP = 650
ARM_DOWN = 10
ARM_BACK = 2000
ARM_PL = 900
    
CLAW= 1
CLAW_OPEN = 300
CLAW_CLOSED = 1622
    
def move_servo_slow(port, start, end, step):
	if start > end:
		step = -step
	for pos in range(start, end, step):
		set_servo_position(port, pos)
		msleep(50)
 	set_servo_position(port, end)
    
def arm_up(step):
  	start = get_servo_position(ARM)
   	move_servo_slow( ARM, start, ARM_UP, step)
        
def arm_down(step):
  	start = get_servo_position(ARM)
	move_servo_slow( ARM, start, ARM_DOWN, step)
        
def arm_back():
	set_servo_position(ARM, ARM_BACK)
  	msleep(750)

def arm_power():
	set_servo_position(ARM, ARM_PL)
  	msleep(750)
 
def close_claw():
	set_servo_position(CLAW, CLAW_CLOSED)
 	msleep(950)
   
def open_claw():
	set_servo_position(CLAW, CLAW_OPEN)
  	msleep(950)
        
def arm_s(step):
  	start = get_servo_position(ARM)
   	move_servo_slow( ARM, start, ARM_SU, step)
        
        
        
        
    