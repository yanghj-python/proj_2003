from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
def index(request):
    print('这是第一个是视图')
    return HttpResponse("Success")
def demo(request):
    print("这是dev分支上的代码")
    return HttpResponse("测试完毕")
def user(request):
    print("this is user")
    return HttpResponse("访问到了user视图")