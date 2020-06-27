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

def ATM():
    print('this is a call for ATM function')

def customer_service():
    print('customer service')



def entertainment():
    print('entertainment and food section')


def departure_file_loaded(session,mws):

    # connect to local MODIM server
    '''
    mws = ModimWSClient()
    mws.setDemoPathAuto(__file__)
    '''
    #session= app.session
    memory_service = session.service('ALMemory')

    '''simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True)
    pepper = simulation_manager.spawnPepper(client,spawn_ground_plane=True)'''

    getDepatureAnswer = memory_service.getData('departureAnswer')
    print('********************Depature Answer is ====>',getDepatureAnswer)

    if getDepatureAnswer == 'ATM':
        mws.run_interaction(ATM)

    elif getDepatureAnswer == 'LFO':
        lfo.load_lfo(session,mws)

    elif getDepatureAnswer == 'FI':
        flight_information.flight_information_load(session,mws)


    elif getDepatureAnswer == 'CST':
        mws.run_interaction(customer_service)

    elif getDepatureAnswer == 'EFC':
        mws.run_interaction(entertainment)
