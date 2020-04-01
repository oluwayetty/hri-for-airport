import os, sys

sys.path.append(os.getenv('PEPPER_TOOLS_HOME')+'/cmd_server')

import pepper_cmd
from pepper_cmd import *

begin()
pepper_cmd.robot.startSensorMonitor()

# wait until front sonar detect something (range < 1.0)
'''
Person in front of the robot (front sonar threshold) -> Pepper says hello
'''
pepper_cmd.robot.say("Where are you? Reveal yourself")
# sonar/sonar_sim.py

personFront = False
personBack = False
while not personFront and not personBack:
    pepper_cmd.robot.setSpeed(0,0,0.5,0.3, False) # only rotation
    p = pepper_cmd.robot.sensorvalue()
    personFront = p[1]>0    # left hand sensor
    personBack = p[2]>0    # right hand sensor

    if personFront:
        pepper_cmd.robot.say("Hello")
    elif personBack:
        pepper_cmd.robot.say("Who is behind me?")

pepper_cmd.robot.stopSensorMonitor()
pepper_cmd.robot.stop()
end()
