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
import customer_service as cs
import entertainment_load


def customer_service():
    print('customer service')


def departure_file_loaded(session,mws,pepper):

    memory_service = session.service('ALMemory')

    getDepatureAnswer = memory_service.getData('departureAnswer')
    print('********************Depature Answer is ====>',getDepatureAnswer)

    if getDepatureAnswer == 'ATM':
        ATM.atm_information_load(session,mws,pepper)
        return True

    elif getDepatureAnswer == 'LFO':
        lfo.load_lfo(session,mws,pepper)
        return True

    elif getDepatureAnswer == 'FI':
        x = flight_information.flight_information_load(session,mws,pepper,conveyor_mode=False)
        return x


    elif getDepatureAnswer == 'CST':
        cs.customerservice_load(session,mws,pepper)
        return True

    elif getDepatureAnswer == 'EFC':
        entertainment_load.entertainment_py_load(session,mws,pepper)
        return False
