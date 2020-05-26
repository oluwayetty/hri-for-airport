import os,sys
import argparse
import qi

pdir=os.getenv('PEPPER_TOOLS_HOME')
sys.path.append(pdir + '/cmd_server')

import pepper_cmd
from pepper_cmd import *

begin()

pepper_cmd.robot.startFaceDetection()
pepper_cmd.robot.saveImage('./test1.jpeg')
#service = pepper_cmd.robot.session_service('ALTabletService')
#print('service called ',service)
end()
