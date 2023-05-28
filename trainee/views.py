from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view python func must accept httprequest as object ,return httpresponse as object

def traineeList(request):
    trainees = [(1,'ahmed'),(2,'mohamed'),(3,'ali')]
    context = {}
    context['trainees']=trainees
    return render(request,'trainee/list.html',context)

def traineeAdd(request):
    return render(request,'trainee/add.html')

def traineeUpdate(request,id):
    return HttpResponse('HI FROM update trainee iti')


def traineeDelete(request,id):
    return HttpResponse('HI FROM delete trainee iti')