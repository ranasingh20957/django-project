from django.shortcuts import render
from SMS.models import *
from .forms import StudentForm,PaymentDetialsFrom
from django.http import HttpResponse

# Create your views here.

def get_student_wise_payment_detial(request):
    if request.method=='GET':
        resp=render(request,'SMS/paymentdetial.html')
        return resp
    elif request.method=='POST':
        sid=int(request.POST.get('txtid',0))
        stu=student.objects.get(id=sid)
        allp=stu.paymentdetials_set.all()
        d1={'payments':allp,'stu':stu}
        resp=render(request,'SMS/paymentdetial.html',context=d1)
        return resp

def course_wise_student_detials(request):
    courses=course.objects.all()
    d1={'courses':courses}
    if request.method=='GET':
        c=course.objects.get(id=2)
        d1['cid']=c.id
        d1['cname']=c.name
        allstu=c.students.all()
        d1['students']=allstu
        resp=render(request,'SMS/studentdetial.html',context=d1)
        return resp
    elif request.method=='POST':
        courseid=request.POST.get('courses')
        c=course.objects.get(id=int(courseid))
        d1['cid']=c.id
        d1['cname']=c.name
        allstu=c.students.all()
        d1['students']=allstu
        resp=render(request,'SMS/studentdetial.html',context=d1)
        return resp

def view_student(request):
    if request.method=='GET':
        frm_unbound=StudentForm()
        d1={'form':frm_unbound}
        resp=render(request,'SMS/studentfrm.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=StudentForm(request.POST,files=request.FILES)
        if frm_bound.is_valid():
           frm_bound.save()
           resp=HttpResponse("<h1>student Registerd SuccessFully!!</h1>")
           return resp
        else:
            d1={'form':frm_bound}
            resp=render(request,'SMS/studentfrm.html',context=d1)
            return resp

def view_payment(request):
    if request.method=='GET':
        frm_unbound= PaymentDetialsFrom()
        d1={'form':frm_unbound}
        resp=render(request,'SMS/paymentfrm.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound= PaymentDetialsFrom(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            resp=HttpResponse("<h1>Payment Saved Successfully<h1>")
            return resp

    else:
        d1={'form':frm_bound}
        resp=render(request,'sms/paymentfrm.html',context=d1)
        return resp  

def view_static(request):
    resp=render(request,'SMS/demostatic.html')
    return resp

def view_student_byid(request,eid):
    if request.method=="GET":
        stu=student.objects.get(id=eid)
        d1={'stu':stu} 
        resp=render(request,'SMS/showstudent.html',context=d1)
        return resp


def get_student(request):
    resp=render(request,'SMS/callapi.html')
    return resp


        
        