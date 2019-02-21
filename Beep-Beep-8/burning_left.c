#include <kipr/botball.h>
#include "library.h"

void burning_left()

{
    //              STAGE 1, AMBULANCE              //
    right(900, 500);
    forward(1100, 1500);
    arm_down();
    claw_open();
    arm_up();
    printf("Stage 1 - Ambulance is complete!")
    // Onward for the fire truck! //
    
    //             STAGE 2, FIRE TRUCK              //
    backward(1100, 6000);
    right(900,200);
    backward(900,560);
    // back of pipe //
    forward(1000, 1700);
    left(1200, 700);   
    drive_to_black(0, THRESH);

    backward(1100, 1500);
    arm_down();
    forward(900, 1000);
    claw_close();
    arm_up();
    // firetruck grabbed! //
    
    backward(900, 200);
    right(900, 200);
    drive_to_black(0, THRESH);
    
    backward(800,50);
    arm_down();
    claw_open();
    arm_up();
    // fire truck scored! //
    printf("Stage 2 - Fire Truck is complete!")
    // onward for fireman #1! //
    
    //             STAGE 3, FIRST FIREMAN              //
    backward(900, 900);
    right(900,200);
    backward_time(1400, 3500);
    // back into pipe //
    forward(1000, 2400);
    left(1000, 850);
    drive_to_black(0, THRESH);
    
    backward(800, 200);
    arm_down();
    forward(900, 700);
    claw_close();
    // grabbed first fireman!
    backward(1000, 500);
    arm_up();
    right(900, 800);
    backward_time(1000, 4000);
    drive_to_black(0, THRESH);   
    left(900, 800);
    forward(900, 2200);
    claw_open();  //  first fireman scored! //
    printf("Stage 3 - First Fireman is complete!")
    // onward for fireman #2! //
    
    //              STAGE 4, SECOND FIREMAN              //
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
    right(900, 500); 
    claw_open(); // score second fireman!! //
    arm_up();
    printf ("Stage 4 - Second Fireman is complete!")
    // onward for fireman #3! //
    
    //              STAGE 5, THIRD FIREMAN              //
    backward_time(900, 2000); 
    // hit back of pipe!
    right(900, 200);
    backward_time(1000, 2000);
    forward(1000, 2300);
    left(1000, 800);
    drive_to_black(0, THRESH);
    arm_down();
    forward(900, 200);
    claw_close();
    backward(900, 200);
    right(900, 500); 
    claw_open(); // score third fireman!!! //
    arm_up();
    printf ("Stage 5 - Third Fireman is complete!")
    // onward for fireman #4! //
    
    //              STAGE 6, FOURTH FIREMAN              //
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
    right(900, 500); 
    claw_open(); // score fourth fireman!!!! //
    arm_up();
    claw_close();
    printf ("Stage 6 - Fourth Fireman is complete!")
    // onward for fireman #5! //
    
    //              STAGE 7, FIFTH FIREMAN              //
    left(900,750);
    arm_down();
    forward(900,200);
    right(900,580); // score fifth fireman!!!!! //
    arm_up(); 
    printf ("Stage 7 - Fifth Fireman is complete!")
    // onward for final realignment //    
    //              STAGE 8, FINAL REALIGNMENT              //
    right(900, 600);
    forward(900,100);
    arm_down();
    left(300, 300);
    printf("Stage 8 - Final Realignment is complete!") 
    
    printf("BEEP BEEP 8 BURNING_LEFT.C IS COMPLETE")     
    

}   
