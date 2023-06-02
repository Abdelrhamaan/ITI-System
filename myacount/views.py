from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from  .models import *

# Create your views here.

def Login(req):
    context = {}
    if (req.method=='POST'):
        # ------------ check email and password------------
        check_user = User.objects.filter(email=req.POST['email'],password=req.POST['password'])
        if (len(check_user) != 0): #????
            # adding user_name to session
            req.session['username'] = check_user[0].user_name
            return HttpResponseRedirect('/trainee')
        else:
            context['message']='Invalid user name or pass'
    return render(req, 'login.html',context=context)


def Logout(req):
    req.session.clear()
    return HttpResponse('Logout')


def Registration(req):
    if(req.method == 'POST'):
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        # ---------first method to set data in database-----------
        # ---------creating and save data in database ----------
        # User.objects.create(user_name=username, email=email, password=password,activ=1)
        # ---------second method to set data in database---------- 
        new_user = User(user_name=username) #????
        new_user.email = email
        new_user.password = password
        new_user.activ = True
        # --------save data in database-----------
        new_user.save()
    return render(req, 'register.html')


# ----- list of all users -------
def user_list(req):
    context={}
    for user in User.objects.all():
        print(user.user_name)
    context['users']=User.objects.all()
    return render(req,'user_list.html',context)