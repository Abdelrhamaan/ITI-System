from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',traineeList,name='traineeList'),
    path('update/<int:id>',traineeUpdate,name='traineeUpdate'),
    path('add',traineeAdd,name='traineeAdd'),
    path('delete/<int:id>',traineeDelete,name='traineeDelete'),
]