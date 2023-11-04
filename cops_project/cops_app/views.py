from django.contrib.auth.models import auth,User
from django.shortcuts import render, redirect
from .models import My_User,Police
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        password=request.POST['password']
        data=My_User.objects.create(first_name=first_name,last_name=last_name,username=username,phone=phone,email=email,address=address,password=password,type=0)
        data.save()
        return redirect(my_login)
    else:
        return render(request,'registration.html')

def my_login(request):
    if request.method=='POST':
        username=request.POST['username']
        Password=request.POST['password']
        try:
            user=My_User.objects.get(username=username, password=Password)
            if user.type == 0:
                request.session['id']=user.id
                return render(request,'profile.html',{'name':user.username})
        except My_User.DoesNotExist:
            police = Police.objects.get(username=username, password=Password)
            request.session['id'] = police.id
            name=police.username
            return render(request, 'police_profile.html',{'name':name})
        except Exception as e:
            return HttpResponse(f" login error {e}")
    else:
        return render(request,'login.html')


def police_login(request):
    return render(request,'police_profile.html')

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(my_login)

def edit(request):
    return render(request,'edit.html')

def edit_police(request):
    return render(request,'edit_police.html')

