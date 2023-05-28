from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
        # course routing
    path('',courseList,name='courseList'),
    path('add',courseAdd,name='courseAdd'),
    path('update/<int:id>',courseUpdate,name='courseUpdate'),
    path('delete/<int:id>',courseDelete,name='courseDelete'),
]