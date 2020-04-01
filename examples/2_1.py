import os, sys

sys.path.append(os.getenv('PEPPER_TOOLS_HOME')+'/cmd_server')

import pepper_cmd
from pepper_cmd import *

begin()

pepper_cmd.robot.say('Hello. How are you?')

vocabulary = ["good", "bad", "well"]
timeout = 30
answer = pepper_cmd.robot.asr(vocabulary, timeout)

# Real ASR will return one word within the vocabulary or ''
if 'good' in answer or 'well' in answer:
    pepper_cmd.robot.say('Great!')
elif 'bad' in answer:
    pepper_cmd.robot.say('Oh, I am sorry')
else:
    pepper_cmd.robot.say('I see you are quite busy')

pepper_cmd.robot.say('Bye bye')

end()
