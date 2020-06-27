import pandas as pd

class flight_information:
    def __init__(self,name_airline,flight_number):
        self.name_airline = name_airline
        self.flight_number = flight_number

    def load_data(self):
        dt = pd.DataFrame(pd.read_csv('../database/flights/flights.csv',usecols=['AIRLINE','FLIGHT_NUMBER','ORIGIN_AIRPORT','DESTINATION_AIRPORT',
        'SCHEDULED_DEPARTURE', 'DEPARTURE_TIME','SCHEDULED_TIME',
        'AIR_TIME','DISTANCE','SCHEDULED_ARRIVAL', 'ARRIVAL_TIME'],nrows=100))

        #dataframe = pd.DataFrame(pd.read_csv('../database/flights/flights.csv'))
        dataframe = dt
        table = pd.DataFrame(dt,columns=['AIRLINE','FLIGHT_NUMBER'])
        loc = table[(table['AIRLINE']==self.name_airline) & table['FLIGHT_NUMBER'].isin([str(self.flight_number)])].index.values

        print(loc)

        if loc.size>0:
            x = loc[0]
            data = dt.iloc[x]
            print('*************************\n',data)






        self.flight_details = dataframe




if __name__ == '__main__':
    airline = raw_input('Enter airline name : ')
    flight_number = raw_input('Enter flight Number')
    fi = flight_information(airline,flight_number   )
    fi.load_data()
