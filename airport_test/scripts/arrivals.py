import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client
import qi
import arrival_movement
import flight_information
import ATM

def goodbye(pepper):
    # im.display.loadUrl('flight_info_showed.html')
    pepper.goToPosture('StandZero',0.2)

    jointsNames = {
    "HeadYaw":0,
    "HeadPitch":-0.2,
    "LShoulderPitch":-0.8,
    "LShoulderRoll":0.7,
    "LElbowYaw":-0.1,
    "LElbowRoll":-1.3,
    "LWristYaw":-0.1,
    "RShoulderPitch":0,
    "RShoulderRoll":0,
    "RElbowYaw":0,
    "RElbowRoll":0,
    "RWristYaw":0,
    "HipRoll":0,
    "HipPitch":0,
    "KneePitch":0
    }
    bye =0
    while bye<10:
        if bye%2==0:
            jointsNames['LShoulderRoll']=-1.2
        else:
            jointsNames['LShoulderRoll']=0.7

        pepper.setAngles(jointsNames.keys(),jointsNames.values(),0.1)
        bye+=1
        time.sleep(1)
    time.sleep(3)
    return

def arrival_file_loaded(session,mws,pepper):

    # connect to local MODIM server
    '''
    mws = ModimWSClient()
    mws.setDemoPathAuto(__file__)
    '''
    #session= app.session
    memory_service = session.service('ALMemory')

    getArrivalAnswer = memory_service.getData('arrivalAnswer')
    print('********************Arrival Answer is ====>',getArrivalAnswer)

    if getArrivalAnswer == 'FT':
        arrival_movement.load_trolley_direction(session,mws,pepper)
        return True
    elif getArrivalAnswer == 'CBL':
        flight_information.flight_information_load(session,mws,pepper,conveyor_mode=True)
        # goodbye(pepper)
        return True
