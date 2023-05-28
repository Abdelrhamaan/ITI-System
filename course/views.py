from django.shortcuts import render
from django.http import HttpResponse
# view python func must accept httprequest as object ,return httpresponse as object

def courseList(request):
    courses = [(1,'django'),(2,'postgres'),(3,'js')]
    context = {}
    context['courses']=courses
    return render(request,'course/list.html',context)


def courseAdd(request):
    return render(request,'course/add.html')

def courseUpdate(request,id):
    return HttpResponse('HI FROM update course iti')


def courseDelete(request,id):
    return HttpResponse('HI FROM delete course iti')