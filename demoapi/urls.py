from django.urls import path

from demoapi.views import view_first_api
from .views import *

#BaseURL=http://127.0.0.1:8000/api/

urlpatterns = [
    path('first/',view_first_api),
    path('getstu/<int:id>/',get_student_by_id)
]
