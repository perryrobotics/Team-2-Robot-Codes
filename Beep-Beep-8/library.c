#include <kipr/botball.h>
#define CLAW  0
#define CLAW_OPEN 500
#define CLAW_HALF 1400
#define CLAW_CLOSED 1650
#define CLAW_PPL 1900

#define ARM 1
#define ARM_BACK 1900
#define ARM_UP 1000
#define ARM_DOWN 210
#define ARM_BUILDING 850

#define LMOTOR 3
#define RMOTOR 0

#define THRESH 3600

#define YELLOW 0
#define LEFT 0
#define RIGHT 1
#define DELAY 500

void backward_time(int speed, int time)
{
    mav(LMOTOR, -speed);
    mav(RMOTOR, -speed);
    msleep(time);
    freeze(LMOTOR);
    freeze(RMOTOR);
    ao();
}
void forward(int speed, int ticks)
{
    cmpc(LMOTOR);
    cmpc(RMOTOR);
    mav(LMOTOR, speed);
    mav(RMOTOR, speed);
    while (gmpc(LMOTOR) < ticks) {}
    freeze(LMOTOR);
    freeze(RMOTOR);
    ao();
    msleep(DELAY);
}


void backward(int speed, int ticks)
{
    cmpc(LMOTOR);
    cmpc(RMOTOR);
    mav(LMOTOR, -speed);
    mav(RMOTOR, -speed);
    while (gmpc(LMOTOR) > -ticks) {}
    freeze(LMOTOR);
    freeze(RMOTOR);
    ao();
    msleep(DELAY);
}


void left(int speed, int ticks)
{
    cmpc(LMOTOR);
    cmpc(RMOTOR);
    mav(LMOTOR, -speed);
    mav(RMOTOR, speed);
    while (gmpc(RMOTOR) < ticks) {}
    freeze(LMOTOR);
    freeze(RMOTOR);
    ao();
    msleep(DELAY);
}


void right(int speed, int ticks)
{
    cmpc(LMOTOR);
    cmpc(RMOTOR);
    mav(LMOTOR, speed);
    mav(RMOTOR, -speed);
    while (gmpc(LMOTOR) < ticks) {}
    freeze(LMOTOR);
    freeze(RMOTOR);
    ao();
    msleep(DELAY);
}
void left_to_black(int port, int thresh)
{
    motor(LMOTOR,-90);
    motor(RMOTOR, 90);
    while (analog(port) < thresh)
    {
        //printf("%d\n", analog(port));
    }
    //printf("WE FOUND BLACK!!");
    freeze(LMOTOR);
    freeze(RMOTOR);
    ao();
}

void drive_to_black(int port, int thresh)
{
    motor(LMOTOR,90);
    motor(RMOTOR, 90);
    while (analog(port) < thresh)
    {
        //printf("%d\n", analog(port));
    }
    //printf("WE FOUND BLACK!!");
    freeze(LMOTOR);
    freeze(RMOTOR);
    ao();
}

void drive_to_white(int port, int thresh)
{
    motor(LMOTOR,90);
    motor(RMOTOR, 90);
    while (analog(port) > thresh)
    {
        //printf("%d\n", analog(port));
    }
    //printf("WE FOUND BLACK!!");
    freeze(LMOTOR);
    freeze(RMOTOR);
    ao();
}

void backwards_to_white(int port, int thresh)
{
    motor(LMOTOR,-90);
    motor(RMOTOR, -90);
    while (analog(port) > thresh)
    {
        //printf("%d\n", analog(port));
    }
    //printf("WE FOUND BLACK!!");
    freeze(LMOTOR);
    freeze(RMOTOR);
    ao();
}

void arm_up()
{
    set_servo_position(ARM, ARM_UP);
    msleep(400);
}

void arm_down()
{
    set_servo_position(ARM, ARM_DOWN);
    msleep(400);
}

void arm_back()
{
    set_servo_position(ARM, ARM_BACK);
    msleep(400);
}

void claw_open()
{
    set_servo_position(CLAW, CLAW_OPEN);
    msleep(400);
}


void claw_close()
{
    set_servo_position(CLAW, CLAW_CLOSED);
    msleep(400);
}

void claw_half()
{
    set_servo_position(CLAW, CLAW_HALF);
    msleep(400);
}


void claw_ppl()
{
    set_servo_position(CLAW, CLAW_PPL);
    msleep(400);
}

void arm_building()
{
    set_servo_position(ARM, ARM_BUILDING);
    msleep(400);
}