#include <kipr/botball.h>
#include "library.h"
#include "burning_left.h"
#include "burning_right.h"



int main()
{
    int side = RIGHT;
    printf("Hello World\n");

    enable_servos();

    //GET IN START POSITION
    arm_back();
    claw_open();
    msleep(3000);
    shut_down_in(119.5);
    //GO DROP AMBULANCE  

    //backward(900, 1500);

    arm_down();
    set_servo_position(0, 1920);
    msleep(300);
    arm_up();
    drive_to_black(0, THRESH);
    drive_to_white(0, THRESH);
    drive_to_black(0, THRESH);
    backwards_to_white(0, THRESH);
    backward(900,400);
    left(1500, 610);
    drive_to_black(0, THRESH);

    camera_open();
    //msleep(100); //Sense the feeling
    int count;
    int x;
    int size;

    for(count =0;count<20; count++)
    {
        size = 0;
        camera_update();
        x = get_object_center_x(0, 0);
        size = get_object_area(0,0);
        if (size > 5000)
        {
            side = LEFT;
        }

        printf("X: %d \tS:%d\n", x,size);
        msleep(50);
    }
    camera_close();
    if (side == LEFT)
    {
        printf("LEFT ON FIRE!!!");
        burning_left();
    }
    else
    {
        printf("RIGHT ON FIRE!!!");
        burning_right();
    }


    disable_servos();
    return 0;
}
