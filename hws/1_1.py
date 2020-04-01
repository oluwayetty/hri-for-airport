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

personHere = False
while not personHere:
    pepper_cmd.robot.setSpeed(0,0,0.5,0.2, False) # only rotation
    p = pepper_cmd.robot.sensorvalue()
    personHere = p[1]>0.0 and p[1]<1.0   # front sonar (0.0 means no value)

pepper_cmd.robot.say("Yasss I see you")

'''
Head touch -> Pepper moves its head up
'''
pepper_cmd.robot.say("Touch my head to start the game")
# touch/touch_sim.py

# wait until head touched
headTouched = False
while not headTouched:
    p = pepper_cmd.robot.sensorvalue()
    headTouched = p[3]>0   # head sensor

pepper_cmd.robot.say("You touched my head, watch me move my head up")
yaw = 0.0 # horizontal, left to right
# pitch = 1.0 #  vertical, up to down
tm = 1.5
pepper_cmd.robot.headPose(yaw,0.5,tm)
pepper_cmd.robot.headPose(yaw,-0.2,tm)
pepper_cmd.robot.headPose(yaw,0.0,tm)

'''
Left/Right hand touch -> Pepper moves its head left/right
'''

pepper_cmd.robot.say("Touch my left or right hand to proceed")
# touch/touch_sim.py

# wait until left or right touched
leftTouched = False
rightTouched = False
while not leftTouched and not rightTouched: #  both of them have to be true
# while not leftTouched or rightTouched:
    p = pepper_cmd.robot.sensorvalue()
    leftTouched = p[4]>0    # left hand sensor
    rightTouched = p[5]>0    # right hand sensor

    response = "left hand" if leftTouched else "right hand"
    if leftTouched or rightTouched:
        pepper_cmd.robot.say("You touched my {}, watch me move my head left to right".format(response))

pitch = 0.0 #  vertical, up to down
tm = 1.5
pepper_cmd.robot.headPose(0.5,pitch,tm)
pepper_cmd.robot.headPose(-0.5,pitch,tm)
pepper_cmd.robot.headPose(0.0,pitch, tm)

pepper_cmd.robot.stopSensorMonitor()
pepper_cmd.robot.stop()
end()
