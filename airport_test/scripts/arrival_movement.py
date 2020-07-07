import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client
import qi
from qibullet import SimulationManager


def trolley_reached():
    im.display.loadUrl('default.html')
    im.executeModality('text_default','This is where you can pick <b> TROLLEYS </b> for your baggages.')


def show_trolley_location(pepper):
    pepper.goToPosture('StandZero',0.2)

    jointsNames = {
    "HeadYaw":0.1,
    "HeadPitch":-0.2,
    "LShoulderPitch":1.5,
    "LShoulderRoll":0,
    "LElbowYaw":0,
    "LElbowRoll":0,
    "LWristYaw":0,
    "RShoulderPitch":1.5,
    "RShoulderRoll":0,
    "RElbowYaw":0,
    "RElbowRoll":0,
    "RWristYaw":0,
    "HipRoll":0,
    "HipPitch":-0.2,
    "KneePitch":0
    }

    pepper.setAngles(jointsNames.keys(),jointsNames.values(),0.2)
    pepper.moveTo(3,5,0.5,speed=15)
    jointsNames['LShoulderPitch']=-0.4
    jointsNames['LShoulderRoll']=0.5
    jointsNames['LElbowYaw']=0.1
    jointsNames['HipPitch']=0
    pepper.setAngles(jointsNames.keys(),jointsNames.values(),0.1)
    time.sleep(3)
    return

def load_trolley_direction(session,mws,pepper):
    show_trolley_location(pepper)
    mws.run_interaction(trolley_reached)