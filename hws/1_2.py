import os, sys, argparse

sys.path.append(os.getenv('PEPPER_TOOLS_HOME')+'/cmd_server')

import pepper_cmd
from pepper_cmd import *

begin()
pepper_cmd.robot.startSensorMonitor()

# wait until front sonar detect something (range < 1.0)
'''
Person in front/back of the robot
'''
# sonar/sonar_sim.py

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sensor", type=str, default="SonarFront",
                        help="Sensor: SonarBack")
    args = parser.parse_args()
    if args.sensor == 'SonarFront':
        front_sonar()
    else:
        back_sonar()

def front_sonar():
    personHere = False

    while not personHere:
        pepper_cmd.robot.setSpeed(0,0,0.5,0.2, False) # only rotation
        p = pepper_cmd.robot.sensorvalue()
        personHere = p[1]>0.0 and p[1]<1.0   # front sonar (0.0 means no value)

    pepper_cmd.robot.say("I see you, touch my left or right hand")

    leftTouched = False
    rightTouched = False
    while not leftTouched and not rightTouched: #  both of them have to be true
        p = pepper_cmd.robot.sensorvalue()
        leftTouched = p[4]>0    # left hand sensor
        rightTouched = p[5]>0    # right hand sensor

        if leftTouched:
            pepper_cmd.robot.say("You touched my left hand, watch me move my head left to right, and raise my left arm")
            move_head_left_to_right()
            pepper_cmd.robot.raiseArm(which = 'L')

        elif rightTouched:
            pepper_cmd.robot.say("You touched my right hand, watch me move my head left to right, and raise my right arm")
            move_head_left_to_right()
            pepper_cmd.robot.raiseArm(which = 'R')


def back_sonar():
    personHere = False

    while not personHere:
        pepper_cmd.robot.setSpeed(0,0,0.5,0.2, False) # only rotation
        p = pepper_cmd.robot.sensorvalue()

        personHere = p[2]>0.0 and p[2]<1.0   # front sonar (0.0 means no value)

    pepper_cmd.robot.say("I see you, touch my head")

    headTouched = False
    while not headTouched:
        p = pepper_cmd.robot.sensorvalue()

        headTouched = p[3]>0    # head sensor

        if headTouched:
            pepper_cmd.robot.say("who's behind me?")

def move_head_left_to_right():
    yaw = 0.0 # horizontal, left to right
    # pitch = 1.0 #  vertical, up to down
    tm = 1.5
    pepper_cmd.robot.headPose(yaw,0.5,tm)
    pepper_cmd.robot.headPose(yaw,-0.2,tm)
    pepper_cmd.robot.headPose(yaw,0.0,tm)

if __name__ == "__main__":
    main()
    pepper_cmd.robot.stopSensorMonitor()
    pepper_cmd.robot.stop()
    end()
