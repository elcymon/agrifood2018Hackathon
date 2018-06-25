from r12.arm import *
import time

SPEED = 3000

is_calibrated = None


def calibrate_initial():
    robot.write('DE-ENERGIZE')
    print("\nPlease manually move the robot in the upright position.")
    raw_input("\nWhen done, press enter to continue...")
    robot.write('ENERGIZE')
    time.sleep(2)
    robot.write('CALIBRATE')
    print(robot.read())
    print("Robot ready to operate\n")


def experiment_set_up():
    time.sleep(2)
    robot.write('TELL SHOULDER 4000 MOVE')
    time.sleep(2)
    robot.write('TELL ELBOW 8500 MOVE')
    time.sleep(2)

def pick():
    time.sleep(2)
    robot.write('CARTESIAN 0 231.5 -162.9 MOVETO')

def back_up():
    time.sleep(2)
    robot.write('CARTESIAN 0 211.8 -63.1 MOVETO')


if __name__ == "__main__":

    # Start r12 and set initial speed
    robot = Arm()
    robot.connect()
    robot.write('START')
    print("Robot starting...")
    time.sleep(2)
    robot.write('{} SPEED !'.format(SPEED))
    print("Setting speed value to {}".format(SPEED))
    print(robot.read())

    #define useful robot variables if need to
    # time.sleep(2)
    # robot.write(': PICK_POS CARTESIAN 0.0 211.8 -63.1 MOVETO ;')  # position to start picking from
    # time.sleep(2)
    # robot.write(': PICK TELL SHOULDER ? ELBOW ? MOVETO ;')  # change position to pick

    try:
        # Calibrate the robot to ensure start from the HOME position
        while is_calibrated not in USER_ANSWERS:
            is_calibrated = raw_input("Is the robot in the upright (home) position? [y/n]")
            if is_calibrated not in USER_ANSWERS:
                print('Please respond with [y/n]')
            elif is_calibrated in ['n','N']:
                calibrate_initial()

        while True:
            cmd = raw_input("write command: ")
            robot.write(cmd)
            time.sleep(.5)
            response = robot.read()
            print(response)

        print("\n\nDisconnecting and exiting...")
        robot.disconnect()

    except e:
        print("The exception was: " + str(e))
        time.sleep(1)
        robot.write('HOME')
        time.sleep(1)
        print("\n\nDisconnecting and exiting...")
        robot.disconnect()
