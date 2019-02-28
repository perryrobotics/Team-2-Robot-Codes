#!/usr/bin/python
import os, sys
from wallaby import *
from motion import *
from effectors import *
from wait_for_start import *

def main():

	print("R2D2 Starting Up!")

	create_connect()

 	#create_full()
 	#wait_for_start(0)
  	shut_down_in(120)
 	enable_servos()
  	arm_back()
	open_claw()
   	#msleep(2000)

        
	#go get first supplies
  	arm_down(60)
  	spin_CW(50, 3)
  	drive_backwards(100, 220) #move towards first supplies
  	spin_CCW(40, 15)
  	close_claw() #Grabbed first supplies
	arm_s(50)
 	spin_CCW(45, 175)
  	arm_down(45)
  	msleep(600)
	claw_s(50) #scoreddddddddddd first supplies
    
    
    #go get second supplies
 	spin_CW(20, 5)
   	arm_up(50)
  	spin_CW(50, 225)  #spin to second supplies
 	arm_down(50)
   	spin_CW(50, 10)
  	drive_backwards(50, 115) #go towards supplies
   	spin_CCW(40, 17)
   	close_claw() # Grab second supplies
   	spin_CW(40, 170)
	msleep(600)
  	claw_s(50)  #yEEEET
    
	#go get third supplies
   	spin_CW(20, 3)
   	arm_up(50)
   	spin_CW(50, 125)#Turn to third pile
   	arm_down(25)
	drive_backwards(50, 145)
	spin_CCW(35, 17) 
   	close_claw()
 	spin_CCW(50, 85) #turn to drop off third pile
	msleep(600)
  	claw_s(50) #Scored THIRD Supplies

    #WUTTTEEER!!! (Take 1) 
	spin_CW(50, 9)
  	arm_up(25)
	spin_CCW(50, 155) #Turn to drive to back pipe WATCH IN TOURNEY!!
  	arm_back()
	drive_backwards (200, 1200)#hit pipe
	drive_straight(100, 340)#get off pipe before turn
   	spin_CW(60, 120)
  	drive_backwards(100,500)
       
	drive_until_black(0,100,2900) #hit the bump, ready to goo get water
	spin_CCW(180,205) #turn to face water poms
	arm_down(60)
	drive_backwards(100, 230) #drive to grab water pile
   	close_claw()# got the first pile
	arm_s(20)

	#grabbed first water pile, go score it now
	spin_CW(50, 80)#spin to face water reclamation unit  WATCH IN TOURNEY
	drive_backwards(55, 95)
	claw_s(50) 
	#WE HAVE SCORED THE FIRST WATER PILE!!! Now lets go get the next one!!!
	  
	drive_straight(150, 450) 
  	#msleep(750) #we did it, we did it, we did it, YAH!!!
   
	#Wuter take 2 ACTION!!!
 	arm_back()
  	spin_CCW(50, 90)
	drive_straight(150, 50)
   	arm_down(45)
	
	
  	drive_backwards(50, 50)
   	close_claw() #Just Grabbed water Now Go score
  	drive_straight(50, 70)
  	arm_s(40)
  	spin_CW(70,80)
	
   	drive_backwards(100, 510)
  	open_claw()
	#scored pile 2, go get 3
	"""
 
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
 	"""
  	disable_servos()
	create_stop()

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()