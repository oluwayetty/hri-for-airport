import os, sys
import time
import qi
import math,random

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client


def ent_selection():
    im.display.loadUrl('enjoy_sel.html')
    while True:
        x = im.ask('enjoy_ask',timeout=50)
        if x != 'timeout':
            break
    im.executeModality('text_default',x.upper()+' IS COMING')
    im.robot.memory_service.insertData('ent_choice',x)

def sayJoke():
    joke = im.robot.memory_service.getData('joke')
    im.executeModality('TTS',joke)
    im.executeModality('text_default',joke)
    time.sleep(5)
    im.executeModality('Buttons',[['yes','Yes, tell me one more..'],['no','No, thats enough']])
    a = im.ask(actionname='',timeout=50)
    if a=='yes':
        im.robot.memory_service.insertData('joke_rep',True)
    else:
        im.robot.memory_service.insertData('joke_rep',False)




def getJoke():
    with open('/home/robot/playground/Airport-Scenario-HRI/airport_test/database/jokes/joke.txt','r') as f:
        jokes=[]
        s=''
        for lines in f:
            if lines.startswith('----'):
                    jokes.append(s)
                    s=''
            else:
                s+=lines
        r = random.randint(0,9)
        return jokes[r]

def dance_together():
    im.display.loadUrl('dance_music.html')
    im.executeModality('text_default','Let\'s Dance Together <br> <b> GO.. GO... GO....')
    im.executeModality('text_music','Please Click the Play Button to play Music')
    
def sing_together():
    im.display.loadUrl('dance_music.html')
    im.executeModality('text_default','Let\'s Sing Together <br> <b> GO.. GO... GO....')
    im.executeModality('text_music','Please Click the Play Button to play Music')
    im.executeModality('buttons',[['return','Thanks, I am pleased....']])
    while True:
        r = im.ask(actionname='',timeout=50)
        if r=='return':
            break

def dance(joints,pepper):

    d=0
    j_lists=[]
    while d<30:
        j_lists=[]
        for j in joints.keys():
            l = joints[j]
            value = random.uniform(l[0],l[1])
            j_lists.append(value)
            #time.sleep(2)
        print('******** D====>',d)
        d+=1
        pepper.setAngles(joints.keys(),j_lists,0.2)
        time.sleep(3)


def stop_music():
    im.display.loadUrl('dance_music.html')

#if __name__=='__main__':
def choose_ent(mws,session,pepper):

    memory_service = session.service('ALMemory')
    mws.run_interaction(ent_selection)
    pepper.goToPosture('StandInit',0.2)
    ent_choice = memory_service.getData('ent_choice')

    if ent_choice == 'joke':
        joke_rep = 'True'
        while joke_rep:
            joke = getJoke()
            memory_service.insertData('joke',joke)
            mws.run_interaction(sayJoke)
            joke_rep = memory_service.getData('joke_rep')
    elif ent_choice=='dance':
        jointLimits ={'HeadYaw': (-2.0857, 2.0857),
                      'HeadPitch': (-0.7068, 0.6371),
                      'LShoulderPitch': (-2.0857, 2.0857),
                      'LShoulderRoll': (0.0087, 1.5620),
                      'LElbowYaw': (-2.0857, 2.0857),
                      'LElbowRoll': (-1.5620, -0.0087),
                      'LWristYaw': (-1.8239, 1.8239),
                      'RShoulderPitch': (-2.0857, 2.0857),
                      'RShoulderRoll': (-1.5620, -0.0087),
                      'RElbowYaw': (-2.0857, 2.0857),
                      'RElbowRoll': (0.0087,1.5620),
                      'RWristYaw': (-1.8239, 1.8239),
                      'HipRoll':(-0.5149,0.5149),
                      'HipPitch':(-1.0385, 1.0385),
                      'KneePitch':(-0.5149,0.5149)
                      }
        mws.run_interaction(dance_together)
        dance(jointLimits,pepper)
        time.sleep(2)
        pepper.goToPosture('StandInit',0.2)
        mws.run_interaction(stop_music)
    elif  ent_choice=='sing':
        mws.run_interaction(sing_together)
        mws.run_interaction(stop_music)


    return True




    #return False
