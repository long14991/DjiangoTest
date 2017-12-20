__author__ = 'QDHL'
#coding=utf-8
#from uiautomator import Device
import subprocess
import time
import Logger
import os
import appiumTest
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
import django
django.setup()
from TestModel.models import Result
from TestModel.models import Details
import appiumServer
import extraction_time
from django.db.models import Avg
import xmlConfig
import desired_capabilities


#获取当前设备列表
def deviceList_get():
    list = []
    output = os.popen('adb devices')
    for line in output.readlines():
        if line.find("device") != -1 and line.find("List") != 0:
            # print line
            device = line[0:len(line) - 7].strip()
            list.append(device)
    print(list)
    return list

#判断当前插入的设备只有一台，如果没有插入或者插入多台则抛出异常
def getDevice():
    lenList = len(deviceList_get())
    if lenList == 0:
        raise Exception("please insert device!")
    elif lenList >1:
        raise Exception("the devices in more than one!")
    else:
        return deviceList_get()[0]

print (getDevice())
#d.screen.on()
print ('点亮屏幕')
#d(text="千丁",className="android.widget.TextView").click()
#print "点击千丁"

#卸载app
def uninstall_apk(packageName):
    output = subprocess.Popen('adb uninstall '+packageName,stdout=subprocess.PIPE,shell=True).communicate()
    #print ('output='+str(output))
    print (output)
    logger.writeLog('卸载应用',str(output))
    if str(output).find('Success')!=-1:
        return True
    else:
        return False

#安装app
def install_apk(path):
    #os.system('adb install C://Users//QDHL//Desktop//apk//hk//3.6//qding-guanjia-qa-release(4).apk')
   # raise Exception("the devices in more than one!")
    #output = os.system('adb install C://Users//QDHL//Desktop//apk//hk//3.6//qding-guanjia-qa-release(4).apk')
    output = subprocess.Popen("adb install "+path,stdout=subprocess.PIPE,shell=True).communicate()
    print (output)
    logger.writeLog('安装应用',str(output))
    if str(output).find('Success')!=-1:
        return True
    else:
        return False


#调用monkerrunner关闭app【废弃】
def closeApp():
    output = os.system('monkeyrunner C://Users//QDHL//PycharmProjects//uiautomarorTest//autoTest.py')
    print ('output='+str(output))
    logger.writeLog('关闭应用',str(output))

#新的线程启动appiumServer
def appiumServerStart():
    t = appiumServer.appiumThread()
    t.start()


#adb shell uiautomator runtest bundle.jar uiautomator-stub.jar -c com.github.uiautomatorstub.Stub
#adb shell am force-stop com.qding.community

#关闭node服务
def nodeClose():
    #os.system('appium -a 127.0.0.1 -p 4723')
    node = os.popen('taskkill /F /IM node.exe')  #windows关闭node服务
    logger.writeLog('关闭node服务',str(node))




#自动化测试步骤
def laugcherTimeTest(i):
    test1 = Result(testId=xmlConfig.getTestId(),log_url=myLogPath)
    test1.save()
    print('卸载应用')
    uninstall = uninstall_apk(xmlConfig.getPackageName())
    print (uninstall)
    print('安装应用')
    tap = install_apk(xmlConfig.getApkPath())
    print (tap)
    clodValue = extraction_time.getStartValue(xmlConfig.getPackageName(),xmlConfig.getActivityName())
    print('coldValue;......'+str(clodValue))
    logger.writeLog('冷启动时间',str(clodValue))
    time.sleep(10)
    os.system('adb shell am force-stop com.qding.community')
    appiumTest.startTest()
    hotValue = extraction_time.getStartValue(xmlConfig.getPackageName(),xmlConfig.getActivityName())
    print('hotValue;......'+str(hotValue))
    logger.writeLog('热启动时间',str(hotValue))
    time.sleep(10)
    save_Values(xmlConfig.getTestId(),i,clodValue,hotValue)
    #appiumTest.startTest()

#将启动时间的数据保存到数据库
def save_Values(testId,time,cold_value,hot_value):
	test1 = Details(testId =testId,time = time,value_cold=cold_value,value_hot=hot_value)
	test1.save()

#获取启动时间的平均值
def average(): #根据testid取执行结果的平均值
	list = 3 #a为江纯传入指定的testId
	num = Details.objects.filter(testId = list).aggregate(Avg('value_keep'))
	num = str(num)
	num = num.split(':',1)[1]
	num = num.split('}', 1)[0]
	print(num)
	return num

def mainTest(packageName,activityName,apkPath,testId):
    xmlConfig.writeXML(packageName,activityName,apkPath,testId)
    global myLogPath
    myLogPath= 'Log//'+str(xmlConfig.getTestId())+'.txt'
    global logger
    logger = Logger.Logger(myLogPath)
    print('关闭appium server')
    nodeClose()
    time.sleep(5)
    print('启动appium server')
    logger.writeLog("启动appium server",'')
    appiumServerStart()
    for i in range(1,3):
        #卸载appiumSetting和unlock是未了适配android7.0及以上版本用的，7.0以下版本不需要卸载
        uninstall_apk('io.appium.settings')
        uninstall_apk('io.appium.unlock')
        logger.writeLog("-----------------测试次数"+str(i),'')
        laugcherTimeTest(i)

mainTest('com.qding.community','com.qding.community.business.home.activity.SplashActivity','C://Users//QDHL//Desktop//apk//qd//3.2//qding-community-qa-_21_-debug(3).apk','20171218')