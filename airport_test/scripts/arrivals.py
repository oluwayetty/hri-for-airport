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
        # arrival_movement.load_trolley_direction(session,mws,pepper)
        arrival_movement.load_transport_mode(session,mws,pepper)
        return True
    elif getArrivalAnswer == 'MAP':
        return True
