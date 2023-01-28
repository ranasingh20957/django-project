from re import I
from django.shortcuts import render
from CMS.models import Customer
# Create your views here.

class Employee:
   def __inti__(self):
      self.name=''
      self.age=0
      self.address=''
      self.mobileno=''
def get_n_Employee(n):
   emp_list=[]
   for i in range(1,n+1):
      emp=Employee()
      emp.name='Deepak'+str(i)
      emp.age=19+i
      emp.address='delhi'
      emp.mobileno='989776778'
      emp_list.append(emp)
   return emp_list   



def view_cus_home(request):
   if request.method=='GET':
      resp=render(request,'CMS/cushome.html')
      return resp
   elif request.method=='POST':
      if 'btnadd' in request.POST:
         cus=Customer()
         cus.name=request.POST.get('txtname','NA')
         cus.age=request.POST.get('txtage','NA')
         cus.address=request.POST.get('txtaddress','NA')
         cus.mobileno=request.POST.get('txtmob','NA')
         cus.save()
         d1={'msg':'Customer Added SuccessFully!!!'}
         resp=render(request,'CMS/cushome.html',context=d1)
         return resp
      elif 'btnsearch' in request.POST:
         cid=int(request.POST.get('txtid',0))
         cus=Customer.objects.get(id=cid)
         d1={'customer':cus}
         resp=render(request,'CMS/cushome.html',context=d1)
         return resp
      elif 'btnupdate' in request.POST:
         cus=Customer()
         cus.id=int(request.POST.get('txtid',0))
         if Customer.objects.filter(id=cus.id).exists():
            cus.name=request.POST.get('txtname','NA')
            cus.age=request.POST.get('txtage','NA')
            cus.address=request.POST.get('txtaddress','NA')
            cus.mobileno=request.POST.get('txtmob','NA')
            cus.save()
            d1={'msg':'Customer Updated SuccessFully!!!'}
            resp=render(request,'CMS/cushome.html',context=d1)
            return resp
      elif 'btndelete' in request.POST:
         cus=Customer()
         cus.id=int(request.POST.get('txtid',0))
         Customer.objects.filter(id=cus.id).delete()
         d1={'msg':'Customer Deleted SuccessFully!!!'}
         resp=render(request,'CMS/cushome.html',context=d1)
         return resp
      elif 'btnshow' in request.POST:
         allcus=Customer.objects.all()
         d1={'customers':allcus}
         resp=render(request,'CMS/cushome.html',context=d1)
         return resp
            
def view_cusall(request):
   resp=render(request,'CMS/cusall.html')
   return resp


def view_dtl(request):
   employees=get_n_Employee(5)
   d1={'a':100,'b':600,'c':900,'employees':employees}
   resp=render(request,'CMS/dtl.html',context=d1)
   return resp   
 