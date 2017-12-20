import os,re,time


def action(cmd):  #执行终端命令
	return_code = os.popen(cmd)
	result = return_code.read()
	return_code.close()
	time.sleep(5)
	return result

def Value(result):  #启动
	cool_values = r'ThisTime: \d*'  # 正则匹配action方法中返回的启动时间
	a = re.compile(cool_values)
	print(result)
	coolLast = re.findall(a, result)
	if len(coolLast)==0:
		return 11000
	a = dispose(coolLast)  #调用dispose方法取出时间
	return a


def dispose(disposeValues): #处理字符串，取出数据并转换类型
	disposeValues = disposeValues.pop()
	disposeValues = int(disposeValues.split(':',1)[1])
	# print('冷启动时间为:{}毫秒'.format(disposeValues))
	return disposeValues


#terminal = 'adb shell am start -W com.qding.community/com.qding.community.business.home.activity.SplashActivity'

def getStartValue(PackageName,ActivityName):
   return Value(action('adb shell am start -W '+PackageName+'/'+ActivityName))
# 调用冷／热启动
# save_hotValues()
# save_coolValues()
# average()

#print(getStartValue())

Value("aaaa")