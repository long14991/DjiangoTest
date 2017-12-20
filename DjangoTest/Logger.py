__author__ = 'QDHL'

import time
import os
class Logger:

    def __init__(self, logName):
        self.logName = logName

    def writeLog(self,tagName,logText):
        global fo
        fo = open(self.logName,'a')
        fo.write(tagName+':\n')
        fo.write(logText+'\n')
        fo.flush()

    def closeLog(self):
        fo.close()

logger = Logger('log.txt')
logger.writeLog("测试",'hahah')


