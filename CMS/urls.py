from django.urls import path
from.views import *

#Base Url ------>> http://127.0.0.1:8000/cms/

urlpatterns = [
path('home/',view_cus_home),
path('allcus/',view_cusall),
path('dtl/',view_dtl)    
]