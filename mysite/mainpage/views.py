from django.shortcuts import render

# Create your views here.

def main_page(request):

    context = {'welcome':'Hi this is my official website'}

    return render(request,'mainpage/main.html',context)
