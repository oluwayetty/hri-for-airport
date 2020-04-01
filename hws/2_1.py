import os, sys, random, argparse

sys.path.append(os.getenv('PEPPER_TOOLS_HOME')+'/cmd_server')

import pepper_cmd
from pepper_cmd import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--value", type=float, default=1.1,
                        help="Sensor measurement")
    parser.add_argument("--duration", type=float, default=3.2,
                        help="Duration of the event")

    args = parser.parse_args()

    sensorChecked = check_parser_values(args.value, args.duration)
    if sensorChecked:
        print('all checked')
        pepper_cmd.robot.dance()

        pepper_get_feedback()
    else:
        pepper_cmd.robot.say("I can't take any action")

def check_parser_values(distance,duration):
    personHere = False
    while not personHere:
        pepper_cmd.robot.setSpeed(0,0,0.5,0.2, False) # only rotation
        p = pepper_cmd.robot.sensorvalue()
        personHere = p[1]>0.0 and p[1]<1.0   # front sonar (0.0 means no value)

    pepper_cmd.robot.say("Yasss I see you now")

    distanceCheck = 1.0 <= distance <= 1.5
    durationCheck = duration > 3
    return personHere and distanceCheck and durationCheck

def pepper_get_feedback():
    pepper_cmd.robot.say("Did you enjoy my performance?")

    vocabulary = ["yes", "no"]
    timeout = 30 # seconds after function returns
    response = pepper_cmd.robot.asr(vocabulary,timeout)
    if response == 'yes':
         pepper_cmd.robot.say("Awesome, I am glad you enjoyed my performance")
    elif response == 'no':
         pepper_cmd.robot.say("Oops, I'm sorry, will do my best next time.")

if __name__ == "__main__":
    begin()
    pepper_cmd.robot.startSensorMonitor()
    pepper_cmd.robot.say("Where are you? Reveal yourself")

    main()

    pepper_cmd.robot.stopSensorMonitor()
    pepper_cmd.robot.stop()
    end()
