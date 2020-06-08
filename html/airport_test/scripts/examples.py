import os, sys

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client
import test

# Definition of interaction functions

def load_modim():
    im.init()
    im.display.loadUrl('index.html')
    im.executeModality('TEXT_title','HRI 2020')
    im.executeModality('TEXT_default','Welcome to FCO Airport!')
    #im.executeModality('BUTTONS',[['yes','Yes'],['no','No']])


def ee_test():
    flag=False
    while True:
        #im.executeModality('TEXT_default','Say Hello Pepper')
        #im.executeModality('IMAGE_default','img/airport_logo.png')
        #im.executeModality('ASR',['Hello Pepper'])
        #pepper_hear = im.ask(actionname=None)
        pepper_hear = im.ask('check_hello_pepper')
        im.executeModality('TEXT_default',pepper_hear)
        #if pepper_hear == 'Hello Pepper':
        if pepper_hear=='correct':
            flag=True
            #return True
            break
    if flag:
        im.display.loadUrl('traveller_choice.html')
        '''im.executeModality('TEXT_default','Hey lets continue Ahead....')
        im.executeModality('TEXT_default','')
        im.executeModality('TEXT_title','')
        '''


def choose_mode():

    im.executeModality('BUTTONS',[['yes','yes go ahead'],['no','no dont go']])
    a = im.ask(actionname='')

    if a =='yes':
        im.display.loadUrl('traveller_choice.html')
        position_passenger = im.ask('passenger_detail')
        if position_passenger =='Departures':
            im.executeModality('TEXT_default',position_passenger)
        elif position_passenger =='Arrivals':
            im.executeModality('TEXT_default',position_passenger)
        elif position_passenger =='Transits ':
            im.executeModality('TEXT_default',position_passenger)


        #im.executeModality('BUTTONS',[['departures','departures'],['arrival','arrival'],['transit','transit']])
        #im.executeModality('Button','img/departures.png')
    else:
        im.init()

# main

if __name__ == "__main__":

    # connect to local MODIM server
    mws = ModimWSClient()
    mws.setDemoPathAuto(__file__)
    flag = False
    # run interaction functions
    mws.run_interaction(load_modim)
    #mws.run_interaction(ee_test)
    mws.run_interaction(choose_mode)

    #mws.run_interaction(e31) # blocking
    #mws.run_interaction(e32)
    #mws.run_interaction(e33)
    #mws.run_interaction(e34)
