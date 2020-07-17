import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client
import qi
from qibullet import SimulationManager
import arrival_movement
import flight_information

def display_transport_information():
    im.display.loadUrl('transport.html')
    im.executeModality('text_default','Here are the ways you can reach your destination from FIO.')
    preferred_transport = im.ask('transport')
    if preferred_transport == 'CAB':
        location = [-2,0,2]
        # pepper.moveTo(-2,4,2)
    elif preferred_transport == "TR":
        location = [-5,0,4]
    return location

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
        return True
    elif getArrivalAnswer == 'TP':
        mws.run_interaction(display_transport_information)
        pepper.moveTo(-2,4,2)
        return True
        # preferred_transport = im.ask('transport')
        # if preferred_transport == 'CAB':
        #     location = [-2,0,2]
        #     pepper.moveTo(-2,4,2)
        #     # return True
        # elif preferred_transport == "TR":
        #     location = [-5,0,4]
        # #     return True
        # elif preferred_transport == "BUS":
        #     location = [-4,0,6]
        # return True

        # arrival_movement.load_trolley_direction(session,mws,pepper)
        # arrival_movement.load_transport_mode(session,mws,pepper)
        return True
    elif getArrivalAnswer == 'MAP':
        arrival_movement.boutique_maps(session,mws,pepper)
        return True
