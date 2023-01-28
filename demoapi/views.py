from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import StudentSerializer

from SMS.models import student
# Create your views here.

@api_view(http_method_names=['GET','POST'])
def view_first_api(request):
    msg="Hello! This is my first API"
    msg=123
    msg=[2,45,'hello',12.8]
    msg=(12,34,56,"ravi")
    msg={1:34.67,"hello":34,4:"right"}
    return Response(data=msg)

@api_view(http_method_names=['GET'])
def get_student_by_id(request,id):    
    stu=student.objects.get(id=id)
    stu_serialize=StudentSerializer(instance=stu)
    resp=Response(data=stu_serialize.data )
    return resp 


