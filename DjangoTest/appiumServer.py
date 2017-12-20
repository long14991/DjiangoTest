__author__ = 'QDHL'
import threading
import os
import subprocess
def appiumServer():
    #os.system('appium -a 127.0.0.1 -p 4723')
    subprocess.Popen('appium -a 127.0.0.1 -p 4723',shell=True)

class appiumThread(threading.Thread):
    def __init__(self,id=None):
        threading.Thread.__init__(self)
        self.id=id
    def run(self):
        appiumServer()
