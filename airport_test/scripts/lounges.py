import os, sys
import time
import qi
import math

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client


def lounges():
    im.display.loadUrl('lounges.html')
    while True:
        x = im.ask('lounges_ask',timeout=50)
        if x != 'timeout':
            break
    im.executeModality('text_default',x)
    im.robot.memory_service.insertData('lounges_answer',x)


def goToLounge():

    l = im.robot.memory_service.getData('lounges_answer')
    im.display.loadUrl('lounges.html')

    if l== 'premiumplaza':
        im.executeModality('text_default','I will show you the <br> <b> Premium Plaza Lounge. </b>')
    elif l == 'primavista':
        im.executeModality('text_default','I will show you the <br> <b> Prima Vista Lounge. </b>')
    elif l == 'casaalitalia':
        im.executeModality('text_default','I will show you the <br> <b> Casa Alitalia Lounge. </b>')


def reachedLounge():
    l = im.robot.memory_service.getData('lounges_answer')
    im.display.loadUrl('display_dest.html')

    if l== 'premiumplaza':
        im.executeModality('image_default','img/premiumplaza.jpg')
    elif l == 'primavista':
        im.executeModality('image_default','img/primavista_dest.jpg')
    elif l == 'casaalitalia':
        im.executeModality('image_default','img/casaalitalia.jpeg')

    im.executeModality('text_default','This is the lounge you have requested. <br> Have a Pleasant Time ')

def moveToLounge(pepper,loungeName):

    pepper.goToPosture('StandInit',0.5)
    JointNames = {
    "HeadYaw":0.1,
    "HeadPitch":-0.2,
    "LShoulderPitch":1.5,
    "LShoulderRoll":0,
    "LElbowYaw":0,
    "LElbowRoll":0,
    "LWristYaw":0,
    "RShoulderPitch":1.5,
    "RShoulderRoll":0,
    "RElbowYaw":0,
    "RElbowRoll":0,
    "RWristYaw":0,
    "HipRoll":0,
    "HipPitch":-0.2,
    "KneePitch":0,
    'LFinger11':0,
    'LFinger12':0,
    'LFinger13':0,
    'RFinger11':0,
    'RFinger12':0,
    'RFinger13':0
    }
    values = pepper.getAnglesPosition(JointNames.keys())

    if loungeName == 'premiumplaza':
        pepper.moveTo(0,0,math.pi,speed=1)
        pepper.moveTo(5,0,0,speed=0.4)
        JointNames["LShoulderPitch"]=-0.4
        JointNames["LShoulderRoll"]=0.5
        JointNames["LFinger11"]=0.9
        JointNames["LFinger12"]=0.9
        JointNames["LFinger13"]=0.9
        pepper.setAngles(JointNames.keys(),JointNames.values(),0.2)

    elif loungeName == 'primavista':

        pepper.moveTo(2,2,0,speed=0.4)
        pepper.moveTo(0,0,math.pi/2,speed=1)

        JointNames["LShoulderPitch"]=-0.4
        JointNames["LShoulderRoll"]=0.5
        JointNames["LFinger11"]=0.9
        JointNames["LFinger12"]=0.9
        JointNames["LFinger13"]=0.9
        pepper.setAngles(JointNames.keys(),JointNames.values(),0.2)

    elif loungeName =='casaalitalia':


        pepper.moveTo(4,-5,0,speed=0.4)
        pepper.moveTo(0,0,-math.pi/6,speed=1)
        JointNames["RShoulderPitch"]=-0.7
        JointNames["RShoulderRoll"]=-1.1
        JointNames["RElbowRoll"]=0.4
        JointNames["RFinger11"]=0.9
        JointNames["RFinger12"]=0.9
        JointNames["RFinger13"]=0.9
        pepper.setAngles(JointNames.keys(),JointNames.values(),0.2)


    time.sleep(3)




#if __name__=='__main__':
def load_lounges(mws,session,pepper):

    fingers={
    'LFinger11':0,'LFinger21':0,'LFinger31':0,'LFinger41':0,
    'LFinger12':0,'LFinger22':0,'LFinger32':0,'LFinger42':0,
    'LFinger13':0,'LFinger23':0,'LFinger33':0,'LFinger43':0,

    'RFinger11':0,'RFinger21':0,'RFinger31':0,'RFinger41':0,
    'RFinger12':0,'RFinger22':0,'RFinger32':0,'RFinger42':0,
    'RFinger13':0,'RFinger23':0,'RFinger33':0,'RFinger43':0,
    }

    memory_service = session.service('ALMemory')
    pepper.setAngles(fingers.keys(),fingers.values(),0.4)

    mws.run_interaction(lounges)

    lounge_name= memory_service.getData('lounges_answer')
    mws.run_interaction(goToLounge)
    moveToLounge(pepper,lounge_name)
    mws.run_interaction(reachedLounge)
    time.sleep(2)
    pepper.goToPosture('StandInit',0.2)
    pepper.setAngles(fingers.keys(),fingers.values(),0.4)
    time.sleep(2)


    return True




    #return False
