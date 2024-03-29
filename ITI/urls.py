"""
URL configuration for ITI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from trainee.views import *
from course.views import *
from myacount.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # ------trainee url routing-------
    path('trainee/',include('trainee.urls')),
    # ------course url routing-----------
    path('course/',include('course.urls')),
    # ------route login ,logout ,reg------
    path('',Login,name='Login'),
    path('Logout',Logout,name='Logout'),
    path('Registration',Registration,name='Registration'),
    # ------user list routing-----------
    path('list/',user_list,name='user_list'),
    
]
