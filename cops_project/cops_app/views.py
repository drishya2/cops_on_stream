from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Case,CustomUser,Notification
from django.http import HttpResponse
from .forms import CopsEditForm,UserForm,UserEditForm,StatusEditForm
from django.contrib.auth.decorators import login_required

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
        pic=request.FILES['pic']
        password=request.POST['password']
        data=CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,phone=phone,email=email,address=address,pic=pic,password=password,user_type=0)
        data.save()
        return redirect(my_login)
    else:
        return render(request,'registration.html')


def police_register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        age=request.POST['age']
        rank=request.POST['rank']
        position=request.POST['position']
        badge_number=request.POST['badge_number']
        service_years=request.POST['service_years']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        password=request.POST['password']
        pic=request.FILES['pic']
        data=CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,age=age,rank=rank,position=position,badge_number=badge_number,service_years=service_years,phone=phone,email=email,address=address,password=password,pic=pic,user_type=1)
        print(data)
        data.save()
        return redirect(my_login)
    else:
        return render(request,'police_registration.html')



def my_login(request):
    if request.method=='POST':
        username=request.POST['username']
        Password=request.POST['password']
        user=authenticate(username=username, password=Password)
        police_officer=CustomUser.objects.filter(user_type=1)
        print(user)

        if user is not None:
            login(request,user)

            if user.user_type==0:
                return redirect(redir_complaint)
            elif user.user_type==1 and user.entry=='approved':
                return redirect(redir_police)
            else:
                return HttpResponse('wait for admins approval')
        else:
            return HttpResponse('invalid loginn credentials')
    else:
        return render(request,'login.html')


def log_out(request):
    logout(request)
    return redirect(my_login)

@login_required(login_url='/edit_police/')
def edit_police(request,id):
    police=CustomUser.objects.get(id=id)
    form = CopsEditForm(instance=police)

    if request.method=='POST':
        form=CopsEditForm(request.POST,request.FILES,instance=police)
        if form.is_valid():
            form.save()
            return render(request,'police_profile.html',{'police':police})
    else:
        return render(request,'edit_police.html',{'form':form,'police':police})

@login_required(login_url='/edit_user/')
def edit_user(request,id):
    user=CustomUser.objects.get(id=id)
    print(user)
    form=UserEditForm(instance=user)
    if request.method=='POST':
        form=UserEditForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return render(request,'complaint.html',{'user':user})
    else:
        return render(request,'edit.html',{'form': form, 'user': user})

@login_required(login_url='/my_profile/')
def my_profile(request,id):
    data=CustomUser.objects.get(id=id)
    return render(request,'my_profile.html',{'data':data})

@login_required(login_url='/file_complaint/')
def file_complaint(request,id):
    user=CustomUser.objects.get(id=id)
    police_officer=CustomUser.objects.filter(user_type=1)
    if request.method=="POST":
        subject=request.POST['subject']
        place=request.POST['place']
        date=request.POST['date']
        culprit=request.POST['culprit']
        victim=request.POST['victim']
        describe=request.POST['describe']
        police_officer_id=request.POST['officer']
        police_officer = CustomUser.objects.get(id=police_officer_id)
        data=Case.objects.create(type=subject,place=place,date=date,culprit=culprit,victim=victim,describe=describe,user=user,police=police_officer)
        data.save()
        return HttpResponse('saved')
    else:
        return render(request,'complaint.html',{'user':user,'police_officer':police_officer})

@login_required(login_url='/show_complaint/')
def show_complaint(request):
    data=CustomUser.objects.get(id=request.user.id)
    print(data)
    case=Case.objects.filter(user=data)
    print(case)
    return render(request,'complaint_view.html',{'data':data,'case':case})

@login_required(login_url='/my_case/')
def my_case(request):
    data=CustomUser.objects.get(id=request.user.id)
    print(data)
    case=Case.objects.filter(police=data)
    print(case)
    return render(request,'my_case.html',{'data':data,'case':case})



@login_required(login_url='/edit_status/')
def edit_status(request,id):
    case=Case.objects.get(id=id)
    print(case)
    form=StatusEditForm(instance=case)
    if request.method=='POST':
        form=StatusEditForm(request.POST,request.FILES,instance=case)
        if form.is_valid():
            form.save()
            return redirect(my_case)
    return render(request,'edit_status.html',{'case':case,'form':form})

@login_required(login_url='/notification/')
def notification(request):
    return render(request,'notification.html')

@login_required(login_url='/police_profile/')
def police_profile(request):
    return render(request,'police_profile.html')

@login_required(login_url='/notification/')
def my_notification(request):
    data=Notification.objects.all()
    return render(request,'notification.html',{'data':data})

def redir_complaint(request):
    user=CustomUser.objects.get(id=request.user.id)
    police_officer=CustomUser.objects.filter(user_type=1)
    return render(request,'complaint.html',{'user':user,'police_officer':police_officer})

def redir_police(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request,'police_profile.html',{'user':user})

def contact(request):
    return render(request,'contact.html')
