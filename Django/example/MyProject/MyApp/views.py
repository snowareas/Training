import sys
from django.shortcuts import render
from django.http import HttpResponse

def Hello(request):
	return HttpResponse("Hello, world!")

def Hello2(request):
	IP = request.META['REMOTE_ADDR']  
	return render(request,'MyApp/Hello.html',{'content':"Hello,{0}".format(IP)})
# Create your views here.
