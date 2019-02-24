#!/usr/bin/python
import os, sys
from wallaby import *
from motion import *
from effectors import *

def main():

	print("R2D2 Starting Up!")
	enable_servos()
	create_connect()

 	#create_full()
  	arm_back()
	open_claw()
   	msleep(2000)
  	shut_down_in(120)
        
	#go get first supplies
  	arm_down(60)
  	spin_CW(50, 3)
  	drive_backwards(100, 248)
  	spin_CCW(40, 7)
  	close_claw()
	arm_s(50)
 	spin_CCW(45, 160)
  	arm_down(45)
  	msleep(600)
	claw_s(50) #scoreddddddddddd
    
    
    #go get second supplies
 	spin_CW(20, 5)
   	arm_up(50)
  	spin_CW(50, 210)
 	arm_down(50)
   	spin_CW(50, 10)
  	drive_backwards(50, 115)
   	spin_CCW(40, 17)
   	close_claw()
   	spin_CW(40, 170)
	msleep(600)
  	claw_s(50)  #yEEEET
    
	#go get third supplies
   	spin_CW(20, 3)
   	arm_up(50)
   	spin_CW(50, 125)
   	arm_down(25)
	drive_backwards(50, 145)
	spin_CCW(35, 17) 
   	close_claw()
 	spin_CCW(50, 78) 
	msleep(600)
  	claw_s(50) #Scored THIRD Supplies

    #WUTTTEEER!!! (Take 1) 
	spin_CW(50, 9)
  	arm_up(25)
	spin_CCW(50, 135) 
  	arm_back()
	drive_backwards (200, 1100)
	drive_straight(100, 360)
   	spin_CCW(60, 105)
	drive_till_bump(100) #hit the bump, ready to goo get water
  	arm_down(60)
	drive_backwards(100, 600) #drive to grab water pile
   	close_claw()
	arm_s(20)
	#grabbed first water pile, go score it now
	spin_CW(50, 83)
	drive_backwards(55, 70)
	claw_s(50) 
	#WE HAVE SCORED THE FIRST WATER PILE!!! Now lets go get the next one!!!
        
	drive_straight(150, 400) 
  	#msleep(750) #we did it, we did it, we did it, YAH!!!
   
	#Wuter take 2 ACTION!!!
 	#arm_back()
  	spin_CCW(50, 90)
   	arm_down(45)
  	drive_backwards(50, 120)
   	close_claw() #Just Grabbed water Now Go score
  	drive_straight(50, 70)
  	arm_s(40)
  	spin_CW(70,91)
   	drive_backwards(100, 420)
  	open_claw()
	#scored pile 2, go get 3
 
	#water 3
	drive_straight(150, 800) 
  	#msleep(750) #we did it, we did it, we did it, YAH!!!
 	#arm_back()
  	spin_CCW(50, 90)
   	arm_down(45)
  	drive_backwards(50, 150)
   	close_claw() #Just Grabbed water Now Go score
  	drive_straight(50, 100)
  	arm_s(40)
  	spin_CW(70,89)
   	drive_backwards(100, 800)
  	claw_s(30)
	arm_back()
  	spin_CCW(100, 20)
  	arm_down(45)
	spin_CW(300, 55)

 	
	
	
   	
    
   
  	disable_servos()

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()