import os, sys
import time

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client
import qi
from qibullet import SimulationManager


def lfo_reached():
    im.display.loadUrl('lfo_reached.html')


def show_lfo_office(pepper):
    pepper.goToPosture('StandZero',0.2)
    joint_names = ["HeadYaw", "HeadPitch",
    "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw",
    "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw",
    "HipRoll","HipPitch","KneePitch"]
    joint_angles = [0.1,-0.2,1.5,0,0,0,0,1.5,0,0,0,0,0,-0.2,0]
    pepper.setAngles(joint_names,joint_angles,0.2)
    pepper.moveTo(6,7,0.5,speed=20)
    joint_angles = [0.1,-0.2,-0.4,0.5,0.1,0,0,1.5,0,0,0,0,0,0,0]
    pepper.setAngles(joint_names,joint_angles,0.1   )
    time.sleep(3)
    return



def load_lfo(session,mws):
#if __name__ == '__main__':
    # connect to local MODIM server

    #session= app.session
    #memory_service = session.service('ALMemory')

    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True)
    pepper = simulation_manager.spawnPepper(client,spawn_ground_plane=True)

    show_lfo_office(pepper)
    simulation_manager.stopSimulation(client)
    mws.run_interaction(lfo_reached)
