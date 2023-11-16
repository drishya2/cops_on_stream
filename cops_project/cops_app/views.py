from django.contrib.auth.models import auth,User
from django.shortcuts import render, redirect
from .models import My_User,Police,Case
from django.http import HttpResponse
from .forms import CopsEditForm,UserForm,UserEditForm

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
        data=My_User.objects.create(first_name=first_name,last_name=last_name,username=username,phone=phone,email=email,address=address,pic=pic,password=password,type=0)
        data.save()
        return redirect(my_login)
    else:
        return render(request,'registration.html')

def my_login(request):
    if request.method=='POST':
        username=request.POST['username']
        Password=request.POST['password']
        try:
            user=My_User.objects.get(username=username, password=Password)   ######
            if user.type == 0:
                request.session['id']=user.id
                return render(request,'complaint.html',{'user':user})
        except My_User.DoesNotExist:
            police = Police.objects.get(username=username, password=Password)
            request.session['id'] = police.id

            return redirect(police_login)
        except Exception as e:
            return HttpResponse(f" login error {e}")
    else:
        return render(request,'login.html')


def police_login(request):
    if 'id' in request.session:
        police_id=request.session['id']
        police=Police.objects.get(id=police_id)
        return render(request,'police_profile.html',{'data':police})

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(my_login)



def edit_police(request,id):
    police=Police.objects.get(id=id)
    form = CopsEditForm(instance=police)

    if request.method=='POST':
        form=CopsEditForm(request.POST,request.FILES,instance=police)
        if form.is_valid():
            form.save()
            return redirect(police_login)
    else:

        return render(request,'edit_police.html',{'form':form,'police':police})

def edit_user(request,id):
    user=My_User.objects.get(id=id)
    form=UserEditForm(instance=user)
    if request.method=='POST':
        form=UserEditForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('my_pofile')
    else:
        return render(request,'edit.html',{'form':form,'user':user})


def my_profile(request,id):
    data=My_User.objects.get(id=id)
    return render(request,'my_profile.html',{'data':data})

def file_complaint(request,id):
    user=My_User.objects.get(id=id)
    if request.method=="POST":
        subject=request.POST['subject']
        place=request.POST['place']
        date=request.POST['date']
        culprit=request.POST['culprit']
        describe=request.POST['describe']
        data=Case.objects.create(type=subject,place=place,date=date,culprit=culprit,describe=describe,user=user)
        data.save()
        return HttpResponse('saved')
    else:
        return render(request,'complaint.html',{'user':user})







