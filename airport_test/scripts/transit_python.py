import os, sys
import time

import lfo
import ATM
import customerService
import entertainment_load



def transit_file_loaded(session,mws,pepper):

    memory_service = session.service('ALMemory')

    getTransitAnswer = memory_service.getData('transitAnswer')
    print('********************Depature Answer is ====>',getTransitAnswer)

    if getTransitAnswer == 'ATM':
        ATM.atm_information_load(session,mws,pepper)
        return True

    elif getTransitAnswer == 'LFO':
        lfo.load_lfo(session,mws,pepper)
        return True

    elif getTransitAnswer == 'CST':
        customerService.customerservice_load(session,mws,pepper)
        return True

    elif getTransitAnswer == 'EFC':
        entertainment_load.entertainment_py_load(session,mws,pepper)
        return False
