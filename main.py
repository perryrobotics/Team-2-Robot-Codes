#!/usr/bin/python
import os, sys
from wallaby import *
from motion import *
from effectors import *

def main():
	enable_servos()
	print "Hello Jani Doot Doot Doot!"
	create_connect()
  	arm_back()
	open_claw()
   	msleep(2000)
        
	#go get first supplies
  	arm_down(50)
  	spin_CW(50, 3)
  	drive_backwards(100, 243)
  	spin_CCW(50, 7)
  	close_claw()
	arm_s(50)
 	spin_CCW(50, 160)
  	arm_down(50)
  	msleep(750)
  	open_claw()  #scoreddddddddddd
    
    
    #go get second supplies
 	spin_CW(20, 5)
   	arm_up(50)
  	spin_CW(50, 210)
 	arm_down(50)
   	spin_CW(50, 10)
  	drive_backwards(50, 115)
   	spin_CCW(50, 17)
   	close_claw()
   	spin_CW(50, 170)
  	open_claw()  #yEEEET
    
	#go get third supplies
   	spin_CW(20, 3)
   	arm_up(50)
   	spin_CW(50, 115)
   	arm_down(25)
	drive_backwards(50, 140)
   	close_claw()
 	spin_CCW(50, 90) 
	msleep(750)
  	open_claw() #Just do it

    #WUTTTEEER!!! (Take 1) 
	spin_CW(20, 5)
  	arm_up(25)
	spin_CCW(50, 140) 
  	arm_back()
	drive_backwards (200, 1110)
	drive_straight(100, 390)
   	spin_CCW(60, 105)
  	arm_down(25)
	drive_backwards(50, 295)
   	close_claw()
	arm_s(20)
	spin_CW(50, 72)
	drive_backwards(55, 60)
	open_claw()
	drive_straight(50, 100) 
  	msleep(750) #we did it, we did it, we did it, YAH!!!
   
	#Wuter take 2 ACTION!!!
 	arm_back()
  	spin_CCW(50, 90)
   	arm_down(45)
  	drive_backwards(50, 120)
   	close_claw()
   	
 	
	
	
   	
    
        
        
	"""
  	msleep(750)
    drive_till_bump(200)
	#drive_backwards(200, 18)
	drive_backwards(200,40)
	spin_CCW(200, 90)
	drive_backwards(75,100)
	drive_till_bump(200)
	drive_backwards(200, 98)
	spin_CCW(200,90) 
	#drive_straight(50, 20)
	drive_straight(50, 180)
	arm_power()
	#PL 1
	spin_CCW(50, 52)
    #PL 2
	spin_CW(50, 30)
	arm_back()
	spin_CW(50,62)
	spin_CCW(100, 140)
	drive_till_bump(200)
	drive_backwards(200, 420)
	spin_CW(50,92)
	drive_backwards(80,300)
	drive_straight(50,20)
	spin_CCW(50,25)
	drive_straight(50,100)
	arm_power()
	spin_CW(50,70)   
    drive_straight(50, 210)
	spin_CCW(50, 70) 
	arm_power()
	spin_CW(50,57)
	spin_CCW(100, 55)
	drive_straight(100, 90)
	arm_power()
	spin_CW(75, 175)
	
	#realign
	spin_CCW(75, 60)
	drive_till_bump(150)
	arm_back()         
	drive_backwards(150, 50) 
	spin_CW(150, 150) 
	drive_backwards(60, 100)
	
	#1st pompom     
 	drive_straight(200, 400)
	spin_CW(100, 210) 
	open_claw()
	arm_down() 
	drive_backwards(100, 205) 
	close_claw() 
	arm_up() 
	spin_CW(100, 45) 
	drive_backwards(100, 250) 
	open_claw()
	#rly quick note since I'm not here, we're planning on having it back into the water tank on the metal bar side diagonally then in goes straight a certain distance and drops the poms. GL :) -Josie 
	"""
	
    
   
    


   	create_disconnect()
  	disable_servos()

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();