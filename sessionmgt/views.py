from datetime import datetime
from itertools import count
from django.shortcuts import render

# Create your views here.
def view_visit_count(request):
    count=request.session.get('count','NA')
    if(count=='NA'):
        count=1
    else:
        count=count+1
    request.session['count']=count    
    d1={'count':count}        
    resp=render(request,'sessionmgt/visit.html',context=d1)
    return resp

def view_writecookie(request):
    if request.method=='GET':
        resp=render(request,'sessionmgt/writecookie.html')
        return resp
    elif request.method=='POST':
        name=request.POST.get('txtname','NA')
        resp=render(request,'sessionmgt/writecookie.html')
        resp.set_cookie(key='name',value=name,max_age=365*24*60*60)
        return resp

def view_readcookie(request):
    if request.method=='GET':
        resp=render(request,'sessionmgt/readcookie.html')
        return resp 
    elif request.method=='POST':
        name=request.COOKIES.get('name','NA')
        if name=='NA':
            d1={"data":"Cookies Not Found!"}
        else:
            d1={"data":name}
        resp=render(request,'sessionmgt/readcookie.html',context=d1)
        return resp        