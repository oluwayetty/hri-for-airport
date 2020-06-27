import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client
import qi
import pandas as pd
import examples as main_export
'''
https://www.kaggle.com/usdot/flight-delays
'''


def flight_information():

    print('flight information')
    im.display.loadUrl('input_flight_information.html')
    im.execute('input_flight_information')
    #time.sleep(1)
    while True:
        im.executeModality('text_airline','Please tell me your airline name')
        im.executeModality('BUTTONS',[['AS','AS'],['AA','AA'],['US','US'],['DL','DL'],['NK','NK'],['AS','AS'],['UA','UA']])
        #im.executeModality('ASR',['quit','Quit','go back'])
        airline_name = im.ask(actionname=None,timeout=50)
        '''if airline_name=='quit':
            im.robot.memory_service.insertData('quit','True')
            break
        '''
        if airline_name!= '' and airline_name!='timeout':
            t = 'The Airline you travelling is '+ airline_name
            im.executeModality('text_airline',t)
            time.sleep(1)
            im.executeModality('text_fn','Please tell me your flight Number')
            im.executeModality('BUTTONS',[['98','98'],['2336','2336']  ,[ '840','840'  ],[ '258','258'  ],[ '135','135'  ],[ '806','806'  ],[ '612','612'  ],['2013','2013'  ],['1112','1112'  ],['1173','1173'  ],['2336','2336'  ],['1674','1674'  ],['1434','1434'  ],['2324','2324'  ],['2440','2440'  ],[ '108','108'  ],['1560','1560'  ],['1197','1197'  ],[ '122','122'  ],['1670','1670'  ],[ '520','520']])
            fn = im.ask(actionname=None,timeout=50)
            if fn!='timeout' and fn!='':
                t = 'The Flight you travelling is '+ fn
                im.executeModality('text_fn',t)
                im.robot.memory_service.insertData('airline_name',airline_name)
                im.robot.memory_service.insertData('flight_number',fn)
                break




def load_data(name_airline,flight_number):
    dt = pd.DataFrame(pd.read_csv('../database/flights/flights.csv',usecols=['AIRLINE','FLIGHT_NUMBER','ORIGIN_AIRPORT','DESTINATION_AIRPORT',
    'SCHEDULED_DEPARTURE', 'DEPARTURE_TIME','SCHEDULED_TIME',
    'AIR_TIME','DISTANCE','SCHEDULED_ARRIVAL', 'ARRIVAL_TIME'],nrows=100))

    #dataframe = pd.DataFrame(pd.read_csv('../database/flights/flights.csv'))
    dataframe = dt
    table = pd.DataFrame(dt,columns=['AIRLINE','FLIGHT_NUMBER'])
    loc = table[(table['AIRLINE']==name_airline) & table['FLIGHT_NUMBER'].isin([str(flight_number)])].index.values

    print(loc)

    if loc.size>0:
        x = loc[0]
        data = dt.iloc[x]
        #print('*************************\n',data)
        return ('done',data)
    else:
        return ('not done',None)


def display_flights_information():
    im.display.loadUrl('flight_information.html')
    get_flight_details = im.robot.memory_service.getData('flights_data')
    get_flight_details = get_flight_details[1:-1].split(',')
    im.executeModality('text_airline',get_flight_details[0])
    im.executeModality('text_fn',get_flight_details[1])
    im.executeModality('text_source',get_flight_details[2])
    im.executeModality('text_destination',get_flight_details[3])
    im.executeModality('text_schdep',get_flight_details[4])
    im.executeModality('text_scharr',get_flight_details[9])
    im.executeModality('text_timedep',get_flight_details[5])
    im.executeModality('text_timearr',get_flight_details[10])
    im.executeModality('text_distance',get_flight_details[8])
    im.executeModality('text_time',get_flight_details[7])


    #['NK',612,'LAS','MSP',25,19.0,181,154.0,1299,526,509.0]


def data_not_found():
    im.executeModality('TEXT_default','Sorry I could not find your flight details')
    im.executeModality('text_airline','')
    im.executeModality('text_fn','')
    time.sleep(1)


'''def getQiApp():
    try:
        connection_url = 'tcp://'+os.environ['PEPPER_IP']+':'+str(9559)
        app = qi.Application(['Say','--qi-url='+connection_url])
        return app
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" +os.environ['PEPPER_IP']+ "\" on port " + str(9559) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
'''

#if __name__=='__main__':
def flight_information_load(session,mws):

    # connect to local MODIM server
    '''
    mws = ModimWSClient()
    mws.setDemoPathAuto(__file__)
    app = getQiApp()
    app.start()
    session = app.session
    '''
    memory_service = session.service('ALMemory')

    mws.run_interaction(flight_information)

    airline_name = memory_service.getData('airline_name')
    flight_number = memory_service.getData('flight_number')

    status ,data_flights = load_data(airline_name,flight_number)
    '''
    AIRLINE                  B6
    FLIGHT_NUMBER          2276
    ORIGIN_AIRPORT          SJU
    DESTINATION_AIRPORT     BDL
    SCHEDULED_DEPARTURE     438
    DEPARTURE_TIME          550
    SCHEDULED_TIME          241
    AIR_TIME                237
    DISTANCE               1666
    SCHEDULED_ARRIVAL       739
    ARRIVAL_TIME            908
    Name: 55, dtype: object
    '''
    if status!='not done':
        x = str(data_flights.tolist())
        print(x)
        memory_service.insertData('flights_data',x)
        mws.run_interaction(display_flights_information)
    else:
        mws.run_interaction(data_not_found)
        mws.run_interaction(flight_information)
