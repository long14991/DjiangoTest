__author__ = 'QDHL'
from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Result

def hello(request):
    content = {}
    content['hello']='hello world by render'
    #return HttpResponse("hello world")
    return render(request,'hello.html',content)

def testdb(request):
    test1 = Result(logPath='D://test//log.txt',timeId='123123')
    test1.save()
    return HttpResponse("添加数据成功")