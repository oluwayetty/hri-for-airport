import os, sys
import time
import qi
import math

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client


def foodcourts():
    im.display.loadUrl('foodcourts.html')
    while True:
        x = im.ask('foodcourts_ask',timeout=50)
        if x != 'timeout':
            break
    im.executeModality('text_default',x)
    im.robot.memory_service.insertData('foodcourts_gate',x)


def goTofoodcourt():

    l = im.robot.memory_service.getData('rest_name')
    g = im.robot.memory_service.getData('rest_gate')
    im.display.loadUrl('foodcourts.html')

    im.executeModality('text_default','I will show you the <br> <b> '+l+' </b> <br><br> which is at <b> Gate '+g+'</b>')


def reachedfoodcourt():
    rest = im.robot.memory_service.getData('rest_name')
    im.display.loadUrl('display_dest.html')

    if rest=='Ferrari Spazio Bollicine':
        im.executeModality('image_default','img/Ferrari Spazio Bollicine.jpg')
    elif rest=='Venchi':
        im.executeModality('image_default','img/venchi.jpg')
    elif rest=='Lavazza Moka':
        im.executeModality('image_default','img/lavazza moka.jpg')

    if rest=='Rossointenso':
        im.executeModality('image_default','img/rossointenso.jpg')

    elif rest=='The Burger Federation':
        im.executeModality('image_default','img/the burger federation.jpg')

    elif rest=='Bistrot':
        im.executeModality('image_default','img/bistroit.jpg')

    elif rest=='RossoSapore':
        im.executeModality('image_default','img/rossasapore.jpg')

    im.executeModality('text_default','This is the restaurant you have requested. <br> <b> Have a Pleasant Time and Enjoy your meal </b>')

def moveTofoodcourt(pepper,foodcourtIndex):

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

    if foodcourtIndex == 0:
        pepper.moveTo(0,0,math.pi,speed=1)
        pepper.moveTo(5,0,0,speed=0.4)
        JointNames["LShoulderPitch"]=-0.4
        JointNames["LShoulderRoll"]=0.5
        JointNames["LFinger11"]=0.9
        JointNames["LFinger12"]=0.9
        JointNames["LFinger13"]=0.9
        pepper.setAngles(JointNames.keys(),JointNames.values(),0.2)

    elif foodcourtIndex==2:

        pepper.moveTo(2,2,0,speed=0.4)
        pepper.moveTo(0,0,math.pi/2,speed=1)

        JointNames["LShoulderPitch"]=-0.4
        JointNames["LShoulderRoll"]=0.5
        JointNames["LFinger11"]=0.9
        JointNames["LFinger12"]=0.9
        JointNames["LFinger13"]=0.9
        pepper.setAngles(JointNames.keys(),JointNames.values(),0.2)

    elif foodcourtIndex ==1:


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

def food_gate():
    im.display.loadUrl('foodcourts.html')
    gate = im.robot.memory_service.getData('foodcourts_gate')
    while True:
        if gate=='B':
            rest = im.ask('food_gateB',timeout=50)
        elif gate=='C':
            rest = im.ask('food_gateC',timeout=50)
        elif gate=='D':
            rest = im.ask('food_gateD',timeout=50)

        if rest!='timeout':
            im.robot.memory_service.insertData('rest_name',rest)
            break

#if __name__=='__main__':
def load_foodcourts(mws,session,pepper):

    fingers={
    'LFinger11':0,'LFinger21':0,'LFinger31':0,'LFinger41':0,
    'LFinger12':0,'LFinger22':0,'LFinger32':0,'LFinger42':0,
    'LFinger13':0,'LFinger23':0,'LFinger33':0,'LFinger43':0,

    'RFinger11':0,'RFinger21':0,'RFinger31':0,'RFinger41':0,
    'RFinger12':0,'RFinger22':0,'RFinger32':0,'RFinger42':0,
    'RFinger13':0,'RFinger23':0,'RFinger33':0,'RFinger43':0,
    }
    gates_rest = ['B8','B5','B3','C9','C4','C8','D4','D5','D2']
    memory_service = session.service('ALMemory')
    pepper.setAngles(fingers.keys(),fingers.values(),0.4)

    mws.run_interaction(foodcourts)
    mws.run_interaction(food_gate)
    rest = memory_service.getData('rest_name')
    gate = memory_service.getData('foodcourts_gate')
    move=0
    if gate=='B':
        if rest=='Ferrari Spazio Bollicine':
            memory_service.insertData('rest_gate',gates_rest[0])
            move=0
        elif rest=='Venchi':
            memory_service.insertData('rest_gate',gates_rest[1])
            move=2
        elif rest=='Lavazza Moka':
            memory_service.insertData('rest_gate',gates_rest[2])
            move=1

    elif gate=='C':
        if rest=='Rossointenso':
            memory_service.insertData('rest_gate',gates_rest[3])
            move=2
        elif rest=='The Burger Federation':
            memory_service.insertData('rest_gate',gates_rest[4])
            move=1
        elif rest=='Bistrot':
            memory_service.insertData('rest_gate',gates_rest[5])
            move=0

    elif gate=='D':
        if rest=='Venchi':
            memory_service.insertData('rest_gate',gates_rest[6])
            move=2
        elif rest=='Rossointenso':
            memory_service.insertData('rest_gate',gates_rest[7])
            move=1
        elif rest=='RossoSapore':
            memory_service.insertData('rest_gate',gates_rest[8])
            move=0


    mws.run_interaction(goTofoodcourt)
    moveTofoodcourt(pepper,move)
    mws.run_interaction(reachedfoodcourt)
    time.sleep(2)
    pepper.goToPosture('StandInit',0.2)
    pepper.setAngles(fingers.keys(),fingers.values(),0.4)
    time.sleep(2)


    return True




    #return False
