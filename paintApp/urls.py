from django.urls import path

from  . import views
from . import routePlot

urlpatterns = [
    path('', views.index, name='index')
]