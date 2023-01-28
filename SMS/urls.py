from django.urls import path
from .views import *

#base url ---> http://127.0.0.1:8000/sms/

urlpatterns=[
path('payment/',get_student_wise_payment_detial),
path('student/',course_wise_student_detials),
path('stufrm/',view_student),
path('payfrm/',view_payment),
path('staticdemo/',view_static),
path('show/<int:eid>/',view_student_byid),
path('ajax/',get_student)
]


