from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
def index(request):
    print('这是第一个是视图')
    return HttpResponse("Success")
