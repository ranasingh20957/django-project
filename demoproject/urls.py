"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from urllib import request
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include,include,include
from django.http import HttpResponse
from django.shortcuts import render
from .import settings
from django.conf.urls.static import static

def view_sum(request,a=0,b=0):
    return HttpResponse("<h1>we are calling sum=</h1>")

def view_sub(request):
    return HttpResponse("<h1>we are calling sub</h1>")

def view_calc(request):
    a=int(request.POST.get('t1',0))
    b=int(request.POST.get('t2',0)) 
    if request.method=='GET':
       d1={'a':a,'b':b}
       resp=render(request,'calc.html',context=d1)
       return resp
    elif request.method=='POST':
        if 'btnsum' in request.POST:
          c=a+b
        elif 'btnsub' in request.POST:
           c=a-b    
        elif 'btnmult' in request.POST:
           c=a*b    
        elif 'btndiv' in request.POST:
            c=a/b
        d1={'a':a,'b':b,'c':c}   
        resp=render(request,'calc.html',context=d1)
        return resp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/<int:a>/<int:b>/',view_sum),
    path('sub/<int:a>/<int:b>/',view_sub),
    path ('calc/',view_calc),
    path('cms/',include('CMS.urls')),
    path('ems/',include('EMS.urls')),      #https://127.0.0.1:8000/ems/
    path('sms/',include('SMS.urls')), 
    path('ems1/',include('EMS1.urls')),     #http://127.0.0.1:8000/ems1/
    path('lms/',include('LMS.urls')),        #http://127.0.0.1:8000/lms/
    path ('api/',include('demoapi.urls')), #http://127.0.0.1:8000/api/
    path('session/',include('sessionmgt.urls')), #http://127.0.0.1:8000/session/
    path('signal/',include('demosignal.urls'))    #http://127.0.0.1:8000/signal/

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

