import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client
import qi
import arrival_movement

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
