import os, sys

sys.path.append(os.getenv('PEPPER_TOOLS_HOME')+'/cmd_server')

import pepper_cmd
from pepper_cmd import *

begin()

pepper_cmd.robot.startSensorMonitor()

pepper_cmd.robot.say("Touch my head to start the game")

# wait until head touched
headTouched = False
while not headTouched:
    p = pepper_cmd.robot.sensorvalue()
    headTouched = p[3]>0   # head sensor

pepper_cmd.robot.say("OK. Now, I'll look for you")
time.sleep(1)

for i in range(3,0,-1):
    pepper_cmd.robot.say(str(i))
    time.sleep(1)

# wait until front sonar detect something (range < 1.0)
personHere = False
while not personHere:
    pepper_cmd.robot.setSpeed(0,0,0.5,0.2, False) # only rotation
    p = pepper_cmd.robot.sensorvalue()
    personHere = p[1]>0.0 and p[1]<1.0   # front sonar (0.0 means no value)

# stop rotation
pepper_cmd.robot.stop()

pepper_cmd.robot.say("Yasssss, I found you")

pepper_cmd.robot.stopSensorMonitor()

end()
