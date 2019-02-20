#include <kipr/botball.h>
#include "library.h"

void burning_left()

{
    right(900, 500);
    forward(1100, 1500);
    arm_down();
    claw_open();
    arm_up();
    // NOW GET FIRETRUCK
    backward(1100, 6000);
    right(900,200);
    backward(900,560);
    forward(1000, 1700);

    left(1200, 700);   

    drive_to_black(0, THRESH);

    backward(1100, 1500);
    arm_down();
    forward(900, 1000);
    claw_close();
    arm_up();
    
    //firetruck scored, get fireman #1
    backward(900, 200);
    right(900, 200);
    drive_to_black(0, THRESH);
    backward(800,50);
    arm_down();
    claw_open();
    arm_up();
    backward(900, 900);
    right(900,200);
    backward_time(1400, 3500);//BACK OF PIPE
    forward(1000, 2400);
    left(1000, 850);
    drive_to_black(0, THRESH);
    backward(800, 200);
    arm_down();

    forward(900, 700);
    claw_close();// GOT FIRST FIREMAN!!  GO SCORE IT!!!
    backward(1000, 500);
    arm_up();
    right(900, 800);
    backward_time(1000, 4000);
    drive_to_black(0, THRESH);   
    left(900, 800);
    forward(900, 2200);
    claw_open();  // FIRST FIREMAN SCORED!!


    ///////////////////////////////////////////////////////
    //		    	GO GET SECOND FIREMAN!!!             //
    ///////////////////////////////////////////////////////
    backward(900, 1000);
    right(900, 600);
    backward_time(1200, 4500); // hit back of pipe
    forward(1000, 2300);
    left(1000, 800);
    drive_to_black(0, THRESH);
    arm_down();
    forward(900, 200);
    claw_close();
    backward(900, 250);
    right(900, 500); // score second fireman!!!
    claw_open();
    arm_up();

    ///////////////////////////////////////////////////////// 
    backward_time(900, 2000); // hit back of pipe!
    right(900, 200);
    backward_time(1000, 2000);
    forward(1000, 2300);
    left(1000, 800);
    drive_to_black(0, THRESH);
    arm_down();
    forward(900, 200);
    claw_close();
    backward(900, 200);
    right(900, 500); // score third fireman!!!
    claw_open();
    arm_up();

    ////////////////////////////////////////////////////////////////
   
    backward_time(900, 2500);
    right(900, 600);
    backward_time(1200, 1500); // hit back of pipe
    forward(1000, 2300);
    left(1000, 800);
    drive_to_black(0, THRESH);
    arm_down();
    forward(900, 200);
    claw_close();
    backward(900, 200);
    right(900, 500); // score fourth fireman!!!
    claw_open();
    arm_up();
    claw_close();
    ///////////////////////////
    left(900,750);
    arm_down();
    forward(900,200);
    right(900,580);
    arm_up();
    right(900, 600);
    forward(900,100);
    arm_down();
    left(300, 300);

    

}   