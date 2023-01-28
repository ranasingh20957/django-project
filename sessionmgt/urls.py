from django.urls import path
from .views import *

#Base URL = #http://127.0.0.1:8000/session/

urlpatterns = [
    path('visit/',view_visit_count),
    path('writecookie/',view_writecookie),
    path('readcookie/',view_readcookie),

]
