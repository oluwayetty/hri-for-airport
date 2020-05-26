import qi
import os,sys
import argparse
import time

def main():

    pepper_ip = os.environ['PEPPER_IP']
    pepper_port = 9559
    # pepper_port = 9559

    try:
        connection_url = 'tcp://'+pepper_ip+':'+str(pepper_port)
        app = qi.Application(['Mood','--qi-url='+connection_url])
    except RuntimeError:
        print('Connection not successful')
        sys.exit(1)

    app.start()

    session = app.session

    tts_service = session.service('ALTextToSpeech')
    mood_session = session.service('ALMood')

    #tts_service.say(' How are you today??')
    print('Subs Info ',mood_session.persons())
    print mood_session.currentPersonState()['valence']['value']

    print mood_session.getEmotionalReaction()

if __name__ == '__main__':
    main()
