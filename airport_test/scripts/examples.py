import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client
import qi
import departure_python
from qibullet import SimulationManager

# Definition of interaction functions

def load_modim():
    im.init()
    im.display.loadUrl('index.html')
    im.executeModality('TEXT_title','HRI 2020')
    im.executeModality('TEXT_default','Welcome to FCO Airport!')
    #im.executeModality('BUTTONS',[['yes','Yes'],['no','No']])


def ee_test():
    flag=False
    im.robot.startSensorMonitor()
    person = False
    while True:
        pepper_hear = im.ask('check_hello_pepper')
        im.executeModality('TEXT_default',pepper_hear)
        front_sensor_value = im.robot.sensorvalue('frontsonar')
        #print('front_sensor_value ',front_sensor_value)
        #if pepper_hear=='correct' and (front_sensor_value <=1 and front_sensor_value>0):
        if pepper_hear == 'correct':
            flag=True
            #return True
            break
    if flag:
        im.display.loadUrl('traveller_choice.html')
        im.robot.memory_service.insertData('beginConv','True')
        im.robot.animation('Hey_1')
    else:
        im.robot.memory_service.insertData('beginConv','False')

def choose_mode():

    im.display.loadUrl('traveller_choice.html')
    position_passenger = im.ask('passenger_detail')
    if position_passenger =='Departures':
        im.executeModality('TEXT_default',position_passenger)
    elif position_passenger =='Arrivals':
        im.executeModality('TEXT_default',position_passenger)
    elif position_passenger =='Transits ':
        im.executeModality('TEXT_default',position_passenger)
    else:
        im.init()

    im.robot.memory_service.insertData('mode',position_passenger)


def departure_operations():
    while True:
        im.display.loadUrl('departures.html')
        departure_choice = im.ask('Departure_details')
        if departure_choice!='timeout':
            im.executeModality('TEXT_default',departure_choice)
            break
    im.robot.animation('Happy_4')
    im.robot.memory_service.insertData('departureAnswer',departure_choice)

def getQiApp():
    try:
        connection_url = 'tcp://'+os.environ['PEPPER_IP']+':'+str(9559)
        app = qi.Application(['Say','--qi-url='+connection_url])
        return app
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" +os.environ['PEPPER_IP']+ "\" on port " + str(9559) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

def test():
    im.robot.startSensorMonitor()
    while True:
        p = im.robot.sensorvalue('frontsonar')
        if p <=1 and p> 0:
            print(p)
            break

if __name__ == "__main__":

    # connect to local MODIM server
    mws = ModimWSClient()
    mws.setDemoPathAuto(__file__)

    app = getQiApp()
    app.start()

    # run interaction functions
    session= app.session
    memory_service = session.service('ALMemory')


    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True)
    pepper= simulation_manager.spawnPepper(client,spawn_ground_plane=True)

    def chec():
        mws.run_interaction(load_modim)
        mws.run_interaction(ee_test)

        getConvCheck = memory_service.getData('beginConv')
        if getConvCheck:
            mws.run_interaction(choose_mode)
        modeCheck = memory_service.getData('mode')
        print('mode got',modeCheck)
        if modeCheck == 'Departures' and getConvCheck:
            mws.run_interaction(departure_operations)
            x = departure_python.departure_file_loaded(session,mws,pepper)
            if not x:
                chec()
            

    chec()
