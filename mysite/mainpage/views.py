from django.shortcuts import render,redirect
from .models import user_service

# Create your views here.

def main_page(request):


    if request.method == "POST":

        print("It is post ....")
        name = request.POST['rname']
        email = request.POST['remail']
        phone = request.POST['rphone']
        whats = request.POST['wphone']
        select = request.POST['myselect']
        text = request.POST['mytext']
        user_object = user_service(name=name,email=email,phone=phone,whats=whats,services = select ,text=text)
        user_object.save()
        print("Object has been saved ......")

        return redirect('/done/')


    context = {'name':"Home"}
    return render(request,'mainpage/index.html',context)


def register_done_page(request):
    context = {}
    get_name = user_service.objects.latest('id')
    context['name'] = get_name
    return render(request,'mainpage/done.html',context)
