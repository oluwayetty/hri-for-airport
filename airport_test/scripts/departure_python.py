import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client
import qi
#from qibullet import SimulationManager
import flight_information
import lfo
import ATM


def customer_service():
    print('customer service')



def entertainment():
    print('entertainment and food section')


def departure_file_loaded(session,mws,pepper):

    # connect to local MODIM server
    '''
    mws = ModimWSClient()
    mws.setDemoPathAuto(__file__)
    '''
    #session= app.session
    memory_service = session.service('ALMemory')

    getDepatureAnswer = memory_service.getData('departureAnswer')
    print('********************Depature Answer is ====>',getDepatureAnswer)

    if getDepatureAnswer == 'ATM':
        x = ATM.atm_information_load(session,mws,pepper)

    elif getDepatureAnswer == 'LFO':
        lfo.load_lfo(session,mws,pepper) 
        return True

    elif getDepatureAnswer == 'FI':
        x = flight_information.flight_information_load(session,mws,pepper)
        return x


    elif getDepatureAnswer == 'CST':
        mws.run_interaction(customer_service)

    elif getDepatureAnswer == 'EFC':
        mws.run_interaction(entertainment)
