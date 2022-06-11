from django.urls import path,include
from .views import *
from . import views
from django.conf import settings

urlpatterns=[
    path('',views.home, name='home'),
]