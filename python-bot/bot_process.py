from sango import Sango
from libs import brew as bw
from services import helpers as hp
import time, subprocess, random as rn

def start():
    if hp.stop_on_command() or (not(hp.start_on_command())):
        print("Please, I cannot start my activity unless give me a command to start, Thank you.")
        print("To be sure of your command kindly type the command "
              "'sango start' or 'sangostart' and copy the command and I will start.\n"
              "Please don't worry whether you typed it in capital or small letters. "
              "After you are done execute me. Thank you.")
    print("Hi, I'm at your service, I'm beginning my activity now!")
    return hp.start_on_command()

def end():
    pass

def execute():
    while True:

        if hp.stop_on_command():
            print("Alright, I'm terminating my activity. I will always be at your service if you need me.")
            subprocess.Popen(['start', 'alarm.wav'], shell=True)
            print('Goodbye :)')
            hp.safe_close_tab()
            break

        if hp.working_time():
            print("Good day!, working time is up: I'm awake!!! :)")
            try:
                btime = [8,10,12,13,15,17,18,20]
                atime = [10,15,20,25,30,35,40,45,50,55,60]
                rn.shuffle(btime)
                rn.shuffle(atime)
                bw.heart_beat(Bot=Sango, data={'user_id': 'ETUS225372'}, 
                              before_interval=rn.choice(btime), 
                              after_interval=rn.choice(atime)*60)
            except Exception as ex:
                if hp.stop_on_command():
                    print("Alright, I'm terminating my activity. I will always be at your service if you need me.")
                    subprocess.Popen(['start', 'alarm.wav'], shell=True)
                    print('Goodbye :)')
                    hp.safe_close_tab()
                    break
                print('An activity was preempted!')
                print(ex)
                print('Continuing preempted activity...')
                Sango.get_instance().preempt(True)
                time.sleep(3)
        else:
            time.sleep(60)
            print("Working time is over: I'm resting ...")