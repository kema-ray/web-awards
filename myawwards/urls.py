from django.urls import path,include
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home, name='home'),
    path('project/', views.new_project,name ='new_project'),
    path('search/', views.search_results, name = 'search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)