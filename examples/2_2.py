import os, sys

sys.path.append(os.getenv('PEPPER_TOOLS_HOME')+'/cmd_server')

import pepper_cmd
from pepper_cmd import *

begin()

pepper_cmd.robot.setArmsStiffness(0.0)
time.sleep(5)
newpose = pepper_cmd.robot.getPosture()
print(newpose)

pepper_cmd.robot.setArmsStiffness(1.0)
pepper_cmd.robot.setPosture(newpose)
