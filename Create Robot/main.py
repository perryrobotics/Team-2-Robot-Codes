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
	#wait_for_start(1)
  	shut_down_in(120)
 	enable_servos()
  	arm_back()
	open_claw()
   	#msleep(2000)

	drive_backwards(100, 50)
	spin_CCW(100, 110)
	drive_till_bump(100) #HIT PIPE NEAR POWER LINES
	spin_CW(100, 90) #TURN TOWARDS BLACK TAPE
	drive_backwards_until_black(200)#DRIVE TO BLACK TAPE
	drive_backwards(200,150)
	spin_CCW_to_black(50)
	spin_CCW(50,20)
	arm_down(50)
 	follow_line(150,1250) #GO DOWN LINE COLLECTING ITEMS IN CLAW
   	#SCORE STUFF INT START BOX
	spin_CCW(100,105)
	drive_backwards(200,210)
	arm_back()
	#SCORED!!  GO GET 1st POM PILE
	spin_CW(100,195)  #SPIN OUT OF BOX TOWARDS 1ST PILE
	drive_backwards(100,50)#DRIVE TOWARDS 1ST PILE
	arm_down(50)
	drive_backwards(100, 200) #DRIVE TOWARDS POMS
	close_claw()  #GRAB 1st POMS
	drive_straight(100,70)#BACK OFF OF PIPES SO WE CAN LIFT POMS
	arm_back()#LIFT POMS
	spin_CW_to_black(100)
 	follow_line(150,1100)

	spin_CCW(100, 50)#TURN TO POM CONTAINER
	#drive_backwards(100, 70)
	arm_up(25)
	claw_s(30)
	#POM PILE 1 SCORED!!  GET #2!
	spin_CCW(100, 75)
	arm_down(50)
	close_claw()#pom pile 2 grabbed
	arm_up(40)
	spin_CW(100,75)
	claw_s(30) #pompile 2 scored
	spin_CCW(100,100)#spin toward pom pile #3
	arm_down(50)
	drive_backwards(100, 300) #drive towards pile #3
	close_claw() #pom pile 3 grabbed
	drive_straight(100, 300)
	arm_up(50)
	spin_CW(100, 105)
	claw_s(30) #pompile 3 scored
	spin_CCW(100, 105) #spin toward pom pile #4
	arm_down(50)
	drive_backwards(100, 600) #drive towards pile #4
	close_claw() #pom pile 4 grabbed
	drive_straight(100, 600)
	arm_up(50)
	spin_CW(100, 112.5)
	claw_s(30) #pompile 4 scored
	arm_back()
	spin_CCW(150, 10)
	arm_down(50)
	drive_backwards(100, 50)
	close_claw()
	spin_CW(500, 180)


	
        
 
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()        
        
        
        
        