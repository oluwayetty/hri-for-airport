import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client




def ATM():
    im.display.loadUrl('ATM_search.html')
    while True:
        bank_name = im.ask('atm_select')
        if bank_name!='timeout':

            im.robot.memory_service.insertData('bank_name',bank_name)
            break

def moveToATM():
    im.executeModality('TEXT_default','Lets Go to ATM <br> TOGETHER')

def reached_atm():
    #im.display.loadUrl('ATM_search.html')
    im.executeModality('TEXT_default','<b>'+im.robot.memory_service.getData('bank_name').upper()+'</b>')
    im.executeModality('text_atmfound','Your requested ATM is HERE')

def pointhand(pepper,hand='left'):

    R_jointsNames = {
    "RShoulderPitch":1.5,
    "RShoulderRoll":0,
    "RElbowYaw":0,
    "RElbowRoll":0,
    "RWristYaw":0
    }
    L_jointNames = {"LShoulderPitch":-0.4,
    "LShoulderRoll":0.5,
    "LElbowYaw":-0.1,
    "LElbowRoll":0,
    "LWristYaw":0
}

    if hand == 'left':
        pepper.setAngles(L_jointNames.keys(),L_jointNames.values(),0.1)
    else:
        pepper.setAngles(R_jointsNames.keys(),R_jointsNames.values(),0.1)
    time.sleep(1)
    return


#if __name__=='__main__':
def atm_information_load(session,mws,pepper):


    memory_service = session.service('ALMemory')

    mws.run_interaction(ATM)
    bank_name = memory_service.getData('bank_name')
    hand='left'
    if bank_name == 'unicredit':
        location = [2,0,0]
        hand='left'
    elif bank_name == 'bancaditalia':
        location = [2,1,0.1]
        hand='left'
    elif bank_name=='bnp':
        location = [5,4,0.2]
        hand='right'
    elif bank_name=='sanpaolo':
        location = [1,4,0.3]
        hand='right'
    elif bank_name=='axis':
        location = [2,6,0.5]
        hand='left'

    mws.run_interaction(moveToATM)

    pepper.moveTo(location[0],location[1],location[2],speed=0.5)
    time.sleep(1)
    pointhand(hand=hand,pepper=pepper)
    mws.run_interaction(reached_atm)
    time.sleep(3)


    mws.run_interaction(atmReached)

    #return False
