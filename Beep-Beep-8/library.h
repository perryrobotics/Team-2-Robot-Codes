#define CLAW  0
#define CLAW_OPEN 500
#define CLAW_CLOSED 1650

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


void backward_time(int speed, int time);
void forward(int speed, int ticks);
void backward(int speed, int ticks);
void left(int speed, int ticks);
void right(int speed, int ticks);
void left_to_black(int port, int thresh);
void drive_to_black(int port, int thresh);
void drive_to_white(int port, int thresh);
void backwards_to_white(int port, int thresh);
void arm_up();
void arm_down();
void arm_back();
void claw_open();
void claw_half();
void claw_close();
void claw_ppl();
void arm_building();
