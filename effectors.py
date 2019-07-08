#!/usr/bin/python
import os, sys
from wallaby import *

ARM = 3
ARM_SU = 510
ARM_UP = 825
ARM_DOWN = 375 #original was 350
ARM_BACK = 2000
ARM_PL = 900
    
CLAW= 1
CLAW_OPEN = 300
CLAW_CLOSED = 1590
CLAW_SU = 300
    
def move_servo_slow(port, start, end, step):
	if start > end:
		step = -step
	for pos in range(start, end, step):
		set_servo_position(port, pos)
		msleep(40)
 	set_servo_position(port, end)
    
def arm_up(step):
  	start = get_servo_position(ARM)
   	move_servo_slow( ARM, start, ARM_UP, step)
        
def arm_down(step):
  	start = get_servo_position(ARM)
	move_servo_slow( ARM, start, ARM_DOWN, step)
        
def arm_back():
	set_servo_position(ARM, ARM_BACK)
  	msleep(350)

def arm_power():
	set_servo_position(ARM, ARM_PL)
  	msleep(350)
 
def close_claw():
	set_servo_position(CLAW, CLAW_CLOSED)
 	msleep(350)
   
def open_claw():
	set_servo_position(CLAW, CLAW_OPEN)
  	msleep(350)
        
def arm_s(step):
  	start = get_servo_position(ARM)
   	move_servo_slow( ARM, start, ARM_SU, step)
      
def claw_s(step):
  	start = get_servo_position(CLAW)
   	move_servo_slow( CLAW, start, CLAW_SU, step)
        
        
        
    