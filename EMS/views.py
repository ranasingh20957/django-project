from doctest import REPORT_ONLY_FIRST_FAILURE
import re
from django.shortcuts import render
from EMS.models import Employes


# Create your views here.

def view_emp_home(request):
   if request.method=='GET':
      resp=render(request,'EMS/emploey.html')
      return resp
   elif request.method=='POST':
      if 'btnadd' in request.POST:
         emp=Employes()
         emp.name=request.POST.get('txtname','NA')
         emp.age=request.POST.get('txtage','NA')
         emp.salary=request.POST.get('txtsalary','NA')
         emp.post=request.POST.get('txtpost','NA')
         emp.address=request.POST.get('txtaddress','NA')
         emp.save()
         d1={'msg':'Employes Added SuccessFully!!!'}
         resp=render(request,'EMS/emploey.html',context=d1)
         return resp
      elif 'btnsearch' in request.POST:
         eid=int(request.POST.get('txtid',0))
         emp=Employes.objects.get(id=eid)
         d1={'employes':emp}
         resp=render(request,'EMS/emploey.html',context=d1)
         return resp
      elif 'btnupdate' in request.POST:
         emp=Employes()
         emp.id=int(request.POST.get('txtid',0))
         if Employes.objects.filter(id=emp.id).exists():
            emp.name=request.POST.get('txtname','NA')
            emp.age=request.POST.get('txtage','NA')
            emp.salary=request.POST.get('txtsalary','NA')
            emp.post=request.POST.get('txtpost','NA')
            emp.address=request.POST.get('txtaddress','NA')
            emp.save()
            d1={'msg':'Employes update Successfully!!'}
            resp=render(request,'EMS/emploey.html',context=d1)
            return resp
      elif 'btndelete' in request.POST:
         emp=Employes()
         emp.id=int(request.POST.get('txtid',0))
         print(emp.id,"empid")
         Employes.objects.filter(id=emp.id).delete()      
         d1={'msg':'Employes Deleteed Successfully !!!'}
         resp=render(request,'EMS/emploey.html',context=d1)
         return resp
      elif 'btnshow' in request.POST:
         allemp=Employes.objects.all()
         d1={'employes':allemp}
         resp=render(request,'EMS/emploey.html',context=d1)
         return resp   


            


def view_empall(request):
    resp=render(request,'EMS/empall.html')
    return resp





