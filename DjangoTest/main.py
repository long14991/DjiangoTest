#此方法是通过命令行方式传参给python脚本
__author__ = 'QDHL'
import argparse
import subprocess
import globalValue
def start():
    parser = argparse.ArgumentParser(description='times of the test')
    parser.add_argument('numbers',type=int,default=1)
    args = parser.parse_args()
    return args.numbers

#print start()   #main.py 3
