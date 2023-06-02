from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# view python func must accept httprequest as object ,return httpresponse as object

def courseList(request):
    #  if user is login continue else redirect to login page
    if('username' in request.session):
        courses = Course.objects.all()
        # courses = [(1,'django'),(2,'postgres'),(3,'js')]
        context = {}
        context['courses']=courses
        print(context['courses'])
        return render(request,'course/list.html',context)
    else:
        return HttpResponseRedirect('/')

def courseAdd(request):
    if('username' in request.session):
        return render(request,'course/add.html')
    else:
        return HttpResponseRedirect('/')

def courseUpdate(request,id):
    return HttpResponse('HI FROM update course iti')


def courseDelete(request,id):
    return HttpResponse('HI FROM delete course iti')