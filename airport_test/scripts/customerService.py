import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client




def customer_service():
    im.display.loadUrl('customerService_search.html')
    while True:
        airlines_name = im.ask('customerservice_action')
        if airlines_name!='timeout':

            im.robot.memory_service.insertData('airlines_name',airlines_name)
            break

def gotoCustomerService():

    airlines_name = im.robot.memory_service.getData('airlines_name')

    im.executeModality('TEXT_default','Lets Go to the  <b> '+airlines_name.upper()+' </b> Customer Service <br> TOGETHER')
    im.executeModality('image_default',im.robot.memory_service.getData('flightImage'))



def reached_customerService():
    #im.display.loadUrl('ATM_search.html')

    im.executeModality('text_csfound','<b>'+im.robot.memory_service.getData('airlines_name').upper()+'</b>')
    im.executeModality('text_default','Your requested Customer Service is HERE')

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
def customerservice_load(session,mws,pepper):


    memory_service = session.service('ALMemory')

    mws.run_interaction(customer_service)
    pepper.goToPosture('StandInit',0.3)
    airlines_name = memory_service.getData('airlines_name')
    hand='left'

    if airlines_name == 'alitalia':
        location = [2,0,0]
        image= 'img/alitalia.jpg'
        hand='left'
    elif airlines_name == 'lufthansa':
        location = [2,1,0.1]
        image= 'img/lufthansa.png'
        hand='left'
    elif airlines_name=='emirates':
        location = [-5,4,0.2]
        image= 'img/emirates.png'
        hand='right'
    elif airlines_name=='etihad':
        location = [-1,4,0.3]
        image= 'img/etihad.png'
        hand='right'
    elif airlines_name=='airfrance':
        location = [-2,6,0.5]
        image= 'img/airfrance.jpg'
        hand='right'

    memory_service.insertData('flightImage',image)
    mws.run_interaction(gotoCustomerService)

    pepper.moveTo(location[0],location[1],location[2],speed=0.5)
    time.sleep(1)
    pointhand(hand=hand,pepper=pepper)

    mws.run_interaction(reached_customerService)
    time.sleep(3)


    #return False
