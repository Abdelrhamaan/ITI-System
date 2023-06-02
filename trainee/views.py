from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from course.models import *

# Create your views here.s
# view python func must accept httprequest as object ,return httpresponse as object

def traineeList(request):
    # trainees = [(1,'ahmed'),(2,'mohamed'),(3,'ali')]
    if('username' in request.session):
        trainees = Trainee.objects.all()
        context = {}
        context['trainees']=trainees
        return render(request,'trainee/list.html',context)
    else:
        return HttpResponseRedirect('/')

def traineeAdd(request):
    if ('username' in request.session):
        context= {}
        context['courses'] = Course.objects.all()
        if (request.method == 'POST'):
            # ------ changing object coming from FK to int --------
            catch = Course.objects.get(id=request.POST['course'])
            # print (catch)
            Trainee.objects.create(name=request.POST['trainee'],course_id = catch)
        return render(request,'trainee/add.html',context)
    else :
        return HttpResponseRedirect('/')
    
    
def traineeDelete(request,id):
    Trainee.objects.filter(id=id).delete()
    return HttpResponseRedirect('/trainee')


def traineeUpdate(request,id):
    context = {}
    context['courses'] =Course.objects.all()
    # print(context['courses'])
    context['traineedata'] = Trainee.objects.get(id=id)
    if (request.method == 'POST'):
        name = request.POST['trainee']
        catch = Course.objects.get(id=request.POST['course'])
        Trainee.objects.filter(id=id).update(name = name,course_id = catch)
        # return HttpResponseRedirect('/trainee')
    return render(request,'trainee/update.html',context)


# context={}
#     context['catagories']=Catagory.objects.all
#     context['taskdata']=Task.objects.get(id=id)
#     if(req.method=='POST'):
#         name=req.POST['taskname']
#         Task.objects.filter(id=id).update(name=req.POST['taskname'],catagoryid=Catagory.objects.get(id=req.POST['catagory']) )
#         return HttpResponseRedirect('/Tasks')