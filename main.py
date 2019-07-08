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
	arm_back()
	wait_for_start(1)
  	shut_down_in(120)
 	enable_servos()
	open_claw()
   	#msleep(2000)

	drive_backwards(100, 50)
	spin_CCW(100, 110)
	drive_till_bump(100) #HIT PIPE NEAR POWER LINES
	spin_CW(100, 90) #TURN TOWARDS BLACK TAPE
	drive_backwards(100,100) #get away from the power box black tape
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
	spin_CW(100,190)  #SPIN OUT OF BOX TOWARDS 1ST PILE==
	drive_backwards(100,50)#DRIVE TOWARDS 1ST PILE
	arm_down(50)
	drive_backwards(100, 200) #DRIVE TOWARDS POMS
	close_claw()  #GRAB 1st POMS
	drive_straight(100,70)#BACK OFF OF PIPES SO WE CAN LIFT POMS
	arm_back()#LIFT POMS
	spin_CW_to_black(100)
	follow_line2(150,1000)
 	follow_line_ET(150,1400)
	msleep(2000)
	drive_straight(100,80)   

	spin_CCW(100, 45)#TURN TO POM CONTAINER (CHANGED FROM #41)
    
    
    
    
    
    


	#drive_backwards(100, 70)
	arm_up(25)
	claw_s(30)
	#POM PILE 1 SCORED!!  GET #2!
	spin_CCW(100, 70)#changed from75
	arm_down(50)
	close_claw()#pom pile 2 grabbed
	arm_up(40)
	spin_CW(100,70)
	claw_s(30) 
	#POM PILE 2 SCORED!! GET #3
	spin_CCW(100,115)#spin toward pom pile #3
	arm_down(50)
	drive_backwards(100, 300) #drive towards pile #3
	close_claw() #pom pile 3 grabbed
	drive_straight(100, 300)
	arm_up(50)
	spin_CW(100, 113)
	claw_s(30) 
	#POM PIlE 3 SCORED!! GET #4
	spin_CCW(100, 120) #spin toward pom pile #4
	arm_down(50)
	drive_backwards(100, 600) #drive towards pile #4
	close_claw() #pom pile #4 grabbed
	drive_straight(100, 620)
	arm_up(50)
	spin_CW(100, 105)
	#drive_straight(100, 20)
	#POM PILE #4 SCORED!!
	claw_s(30)#POM PILE #4 SCORED!!
	#grab the continer
	spin_CW(100, 5)
	drive_straight(100, 30)
	arm_down(50)
	drive_backwards(100, 140)
	set_servo_position(CLAW, 930) #Grab container
	msleep(1000)
	drive_straight(100, 500)
	spin_CW(100, 65)
	drive_backwards(100, 300)
	#open_claw()
	#drive_straight(100, 150)
	#spin_CCW(100, 30)
	#arm_up(50)
	#drive_backwards(100, 400)
        
	#arm_back()
	#spin_CCW(150, 10)
	#arm_down(50)
	#drive_backwards(100, 50)
	#close_claw()
	#spin_CW(500, 180)


	
       
 
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()        
        
        
        
        