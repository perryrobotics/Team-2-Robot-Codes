#!/usr/bin/python
import os, sys
from wallaby import *
from motion import *
from effectors import *
from wait_for_start import *

def main():

	print("R2D2 Starting Up!")

	create_connect()

 	create_full()
 	#wait_for_start(0)
  	shut_down_in(120)
 	enable_servos()
  	arm_back()
	open_claw()
   	#msleep(2000)

        
	#go get first supplies
  	arm_down(60)
	spin_CW(50, 3)
  	drive_backwards(100, 170) #move towards first supplies
  	spin_CCW(40, 3)
  	close_claw() #Grabbed first supplies
	arm_s(50)
 	spin_CCW(45, 140) #turn into starting box
  	arm_down(45)
  	msleep(600)
	claw_s(50) #scoreddddddddddd first supplies
 	spin_CW(100, 5)
   	arm_up(50)
	#go get second supplies
  	spin_CW(50, 183)  #spin to second supplies
 	arm_down(50)
   	#spin_CW(50, 10)
  	drive_backwards(50, 170) #go towards supplies
   	spin_CCW(40, 10)
   	close_claw() # Grab second supplies
   	spin_CW(40, 150)
	msleep(600)
  	claw_s(50)  #SCORE 2nd SUPPLIES
	

   	spin_CW(100, 5)
	arm_up(50)
	#go get third supplies
   	spin_CW(50, 105)#Turn to third pile
   	arm_down(25)
	drive_backwards(50, 145)
	spin_CCW(35, 17) 
   	close_claw()
 	spin_CCW(50, 75) #turn to drop off third pile
	msleep(600)
  	claw_s(50) #Scored THIRD Supplies
    
	arm_up(75)
  	spin_CW(100, 75)
	drive_backwards(100,100)
	spin_CW(100,80) #Turn to face water pile
	arm_down(40)
	drive_backwards(100, 150)
  	spin_CCW(50,10)
	close_claw()
	drive_straight(100, 140)
	arm_up(50)
	spin_CCW(100, 85)
	drive_till_bump(250)#hip pipe by PL
	drive_backwards(100, 400)
	spin_CCW(100,90)
	drive_backwards(100,600)#hit pipe by pvc 
	drive_until_black(0,100, 3000)
	spin_CCW(100,100) 
	drive_backwards(100,550)#Hit pipe a second time
	drive_straight(100, 305)
 	spin_CCW(100, 47)
  	arm_s(40)
 	drive_backwards(100, 50)
  	claw_s(40)
	spin_CCW(100, 65)
	arm_down(40)
 	drive_backwards(100, 170)
 	close_claw()
	arm_s(40)
 	drive_straight(100, 170)
  	spin_CW(100, 65)
  	claw_s(50)
	spin_CCW(100,90)
	arm_down(40)
	drive_backwards(100,380)
	close_claw()
	drive_straight(100,380)
	arm_s(40)
	spin_CW(100,86)
	claw_s(40)
	close_claw()
	arm_back()
	spin_CCW(100, 60) 
	drive_backwards(100, 300)
	spin_CW(100, 70) 
	arm_down(50)
	spin_CW(500,55) 
	

  	disable_servos()
	create_stop()

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()