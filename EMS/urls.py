from django.urls import path
from .views import *

#base url ---> http://127.0.0.1:8000/ems/

urlpatterns = [

path('home/',view_emp_home),
path('allemp/',view_empall)

]