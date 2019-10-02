from django.shortcuts import render,redirect
from .models import user_service
from .forms import RegisterForm ,AddingRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
# Create your views here.


def main_page(request):
    loged_in_user = request.user

    context = {'name':"Home" ,'user_name':loged_in_user }
    return render(request,'mainpage/index.html',context)

@login_required(login_url = '/login/')
def register_done_page(request):
    context = {}
    get_name = user_service.objects.filter(author = request.user)

    try:
        latest_object = user_service.objects.filter(author = request.user).order_by('-id')[0]
    except:
        latest_object = ''

    loged_in_user = request.user
    context = {'name':get_name ,'lastObject':latest_object,'user_name':loged_in_user }
    return render(request,'mainpage/done.html',context)


@login_required(login_url = '/login/')
def payment_done_page(request):
    context = {}
    get_name = user_service.objects.filter(author = request.user)

    try:
        latest_object = user_service.objects.filter(author = request.user).order_by('-id')[0]
    except:
        latest_object = ''

    loged_in_user = request.user
    context = {'name':get_name ,'lastObject':latest_object,'user_name':loged_in_user }
    return render(request,'mainpage/payment.html',context)

def mypayment(request):
    context = {}
    return render(request,'mainpage/mypayment.html',context)


def user_signup_page(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('user_page')
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(request,'mainpage/signup.html',context)

def log_in_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('mainpage')

    else:
        form = AuthenticationForm()
    context = {'form':form}

    return render(request,'mainpage/login.html',context)

def log_out_page(request):
    logout(request)
    return redirect('/')

@login_required(login_url = '/login/')
def user_page(request):

    if request.method == "POST":
        form = AddingRequest(request.POST , request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('/done/')
    else:
        form = AddingRequest()


    loged_in_user = request.user

    context = {'user_name':loged_in_user , 'form':form}
    return render(request,'mainpage/user.html',context)

@user_passes_test(lambda u: u.is_superuser)
def control_page(request):
    one_objs = user_service.objects.all()
    context = {'one_objs':one_objs}
    return render(request,'mainpage/control.html',context)
