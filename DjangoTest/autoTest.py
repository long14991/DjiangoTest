#使用monkeyrunner进行关闭应用操作，测试过程中发现当出现系统权限弹出框后，导致无法关闭应用。废弃次方法
from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner import MonkeyDevice
from com.android.monkeyrunner import MonkeyImage
import time
device=MonkeyRunner.waitForConnection()
device.press('KEYCODE_BACK','DOWN_AND_UP')
time.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')


