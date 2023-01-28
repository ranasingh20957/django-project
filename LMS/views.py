from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorator import check_authenticated

# Create your views here.
def view_home(request):
    resp=render(request,'LMS/home.html')
    return resp

@check_authenticated
def view_register(request):
    if request.method=='GET':
        frm_unbound=UserCreationForm()
        d1={'form':frm_unbound}
        resp=render(request,'LMS/register.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=UserCreationForm(request.POST)
        if frm_bound.is_valid():
            u=frm_bound.save()
            u.is_staff=True
            u.save()
            g=Group.objects.get(id=1)
            u.groups.add(g)
            return HttpResponse("<h1>User Register SuccessFully!!</h1>")
    else:
        d1={'form':frm_bound}
        resp=render(request,'LMS/register.html',context=d1)
        return resp    

@check_authenticated
def view_login(request):
    if request.method=='GET':
        resp=render(request,'LMS/login.html')
        return resp
    elif request.method=='POST':
        u_user=request.POST.get('user','NA')
        u_pass=request.POST.get('pwd','NA')
        u=authenticate(request,username=u_user,password=u_pass)
        if u is not None:
            login(request,user=u)
            return redirect('home')
        else:
            return redirect('login')


@login_required(login_url='login')
def view_secure1(request):
    resp=render(request,'LMS/secure1.html')
    return resp 
    
@login_required(login_url='login')
def view_secure2(request):
    resp=render(request,'LMS/secure2.html')
    return resp

def view_unsecure1(request):
    resp=render(request,'LMS/unsecure1.html')
    return resp

def view_unsecure2(request):
    resp=render(request,'LMS/unsecure2.html')
    return resp  

def view_logout(request):
    logout(request=request)
    resp=render(request,'LMS/logout.html')
    return resp