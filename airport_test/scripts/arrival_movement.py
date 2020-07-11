import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client
import qi
from qibullet import SimulationManager
from ATM import pointhand

def walk_to_trolley():
    im.display.loadUrl('default.html')
    im.executeModality('text_default',' Please follow me to reach <br> the <b> TROLLEYS LOCATION </b>')
    time.sleep(2)

def trolley_reached():
    im.display.loadUrl('default.html')
    im.executeModality('text_default','This is where you can pick <b> TROLLEYS </b> for your baggages.')

def show_trolley_location(pepper,x,y,z):
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
    pepper.moveTo(x,y,z,speed=15)
    jointsNames['LShoulderPitch']=-0.4
    jointsNames['LShoulderRoll']=0.5
    jointsNames['LElbowYaw']=0.1
    jointsNames['HipPitch']=0
    pepper.setAngles(jointsNames.keys(),jointsNames.values(),0.1)
    time.sleep(3)
    return

def display_transport_information():
    im.display.loadUrl('transport.html')
    im.executeModality('text_default','Here are the ways you can reach your destination from FIO.')
    preferred_transport = im.ask('transport')
    if preferred_transport == 'CAB':
        location = [-2,0,2]
        mws.run_interaction(show_trolley_location(pepper,-2,0,2))
        # return True
    elif preferred_transport == "TR":
        location = [-5,0,4]
    #     return True
    elif preferred_transport == "BUS":
        location = [-4,0,6]
    # return True

def load_trolley_direction(session,mws,pepper):
    mws.run_interaction(walk_to_trolley)
    show_trolley_location(pepper,3,5,0.5)
    mws.run_interaction(trolley_reached)

def load_transport_mode(session,mws,pepper):
    mws.run_interaction(display_transport_information)
    # move(pepper)
