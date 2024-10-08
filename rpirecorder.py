import subprocess
from time import sleep
#import signal
from datetime import datetime
from threading import Thread

date = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

cmd = [
    'arecord',
    '-f',
    'cd',
    date + '.mp3'
    ]

# start recording
def rec_start():
    print("recording")
    subprocess.run(cmd)#-D hw:2,0 -d 5 -f cd test.wav -c 1
    
    
# stop recording
def rec_stop():
    subprocess.run(['pkill','arecord'])
#p.send_signal(signal.SIGINT)
    print('recording finished')

Thread(target=rec_start).start()
sleep(10)
rec_stop()
