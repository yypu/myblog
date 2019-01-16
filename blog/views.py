from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # 首先接受请求
    return HttpResponse("Hello, world")

