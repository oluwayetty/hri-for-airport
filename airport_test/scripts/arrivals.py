import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client
import qi
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

    # if getDepatureAnswer == 'FT':
    #     x = ATM.atm_information_load(session,mws,pepper)
    #
    # elif getDepatureAnswer == 'CBL':
    #     lfo.load_lfo(session,mws,pepper)
    #     return True
