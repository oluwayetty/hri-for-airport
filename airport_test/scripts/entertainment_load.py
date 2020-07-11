import os, sys
import time
import ent
import lounges
import foodcourts
import math
pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client




def load_entertainment():
    im.display.loadUrl('entertainment_selection.html')
    x = im.ask('entertainment_ask')
    im.robot.memory_service.insertData('entertainment_answer',x)


def entertainment_py_load(session,mws,pepper):

    memory_service = session.service('ALMemory')
    try:
        mws.run_interaction(load_entertainment)
        ent_answer = memory_service.getData('entertainment_answer')
        if ent_answer=='lounges':
            lounges.load_lounges(mws,session,pepper)
        elif ent_answer== 'foodcourts':
            foodcourts.load_foodcourts(mws,session,pepper)
        elif ent_answer == 'entertainment':
            ent.choose_ent(mws,session,pepper)
    except Exception as e:
        print('Error occured',e)

    #return False
