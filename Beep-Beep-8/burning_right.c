#include <kipr/botball.h>
#include "library.h"

void burning_right()
{
    backward(1000, 500);
    arm_down();
    claw_open();
    arm_up();
    // AMBULANCE SCORED! GET FIRE TRUCK!!

    backward(900, 1500);
    right(900,700);
    backward_time(1200, 4000);//back into the pipe//
    forward(1000, 1500);
    left(900, 800);
    drive_to_black(0, THRESH);
    backward(900, 500);
    arm_down();  
    claw_close();
    arm_up(); // GOT FIRETRUCK, SCORE IT NOW!
    right(900, 700);
    drive_to_black(0, THRESH);
    forward(1000, 1000);
    left(900, 150);
    forward(900, 800);
    arm_down();
    claw_open();
    arm_up();
    //FIRE TRUCK HAS LANDED!!!
    //GO GET FIRST FIREFIGHTER, MAKE IT AIRBORNE!!!
    backward(900, 2100);
    right(900, 350);

    //Go get first fireman
    backward(1500, 6000);//hit pipe
    forward(1000, 2300);
    left(1000, 850);
    drive_to_black(0, THRESH);
    right(500, 25);
    arm_down();
    forward(900, 200); //go forward towards first fireman//
    claw_close();
    backward(1000, 500);
    arm_up();
    right(900, 700);
    drive_to_black(0, THRESH);
    drive_to_white(0, THRESH);
    forward(1000, 1500);
  	left(900, 200);
    arm_down();
	claw_half();
    arm_up();
    claw_open();
    //we have scored fireman number 1 lets score number 2 !!
    right(1000, 150);
    backward(1500, 6500);// HIT PIPE!!!
    forward(1000, 2300);
    left(1000, 850);
    drive_to_black(0, THRESH);
    right(500, 25);  
    arm_down();
    forward(900, 500);
    claw_close();
    backward(1000, 500);
    arm_up();
    right(900, 700);
    drive_to_black(0, THRESH);
    drive_to_white(0, THRESH);
    forward(1000, 1300);

    arm_down();
    left(900, 200);
    claw_half();
    arm_up();
    claw_open();
    //fireman 2 scored lets score the third one
    right(1000, 75);
    backward(1500, 6500); // HIT PIPE
    forward(1000, 2300);
    left(1000, 850);
    drive_to_black(0, THRESH);
    right(500, 25);
    arm_down();
    forward(900, 500);
    claw_close();
    backward(1000, 600);
    arm_up();
    right(900, 700);
    drive_to_black(0, THRESH);
    drive_to_white(0, THRESH);
    forward(1000, 1500);
  	arm_down();
    left(900, 200); //fireman on the area, claw stays on the block//
  // ATTENTION! ALL FIREMAN HAVE BEEN SCORED! I REPEAT ALL FIREMAN HAVE BEEN SCORED!
    claw_half();
    arm_up();
    right(900, 200);
    arm_down();
	backward(900, 500);
    right(1200,1100);
    forward(1200, 1300);
    left(1500,800);
    forward(1000, 2300);
    claw_ppl();
    backward(1500, 2300);
}
