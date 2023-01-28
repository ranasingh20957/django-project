import re
from django.shortcuts import render
from EMS1.models import Employes


# Create your views here.
def view_emp(request):
   if request.method=='GET':
      resp=render(request,'EMS1/empapp.html')
      return resp
   elif request.method=='POST':
      if 'btnadd' in request.POST:
         emp1=Employes()
         emp1.name=request.POST.get('txtname','NA')
         emp1.age=request.POST.get('txtage','NA')
         emp1.mobileno=request.POST.get('txtmobileno','NA')
         emp1.city=request.POST.get('txtcity','NA')
         emp1.address=request.POST.get('txtaddress','NA')
         emp1.img=request.POST.get('textimg','NA')
         emp1.save()
         d1={'msg':'Employes Added SuccessFully!!!'}
         resp=render(request,'EMS1/empapp.html',context=d1)
         return resp

   elif 'btnsearch' in request.POST:
         eid=int(request.POST.get('txtid',0))
         emp1=Employes.objects.get(id=eid)
         d1={'employes':emp1}
         resp=render(request,'EMS1/empapp.html',context=d1)
         return resp
   elif 'btnupdate' in request.POST:
         emp1=Employes()
         emp1.id=int(request.POST.get('txtid',0))
         if Employes.objects.filter(id=emp1.id).exists():
            emp1.name=request.POST.get('txtname','NA')
            emp1.age=request.POST.get('txtage','NA')
            emp1.mobileno=request.POST.get('txtmobileno','NA')
            emp1.city=request.POST.get('txtcity','NA')
            emp1.address=request.POST.get('txtaddress','NA')
            emp1.img=request.POST.get('txtimg','NA')
            emp1.save()
            d1={'msg':'Employes update Successfully!!'}
            resp=render(request,'EMS1/empapp.html',context=d1) 
            return resp
   elif 'btndelete' in request.POST:
         emp1=Employes()
         emp1.id=int(request.POST.get('txtid',0))
         print(emp1.id,"emp1id")
         Employes.objects.filter(id=emp1.id).delete()      
         d1={'msg':'Employes Deleteed Successfully !!!'}
         resp=render(request,'EMS1/empapp.html',context=d1)
         return resp
   elif 'btnshow' in request.POST:
         allemp=Employes.objects.all()
         d1={'employes':allemp}
         resp=render(request,'EMS1/empapp.html',context=d1)
         return resp   

     



