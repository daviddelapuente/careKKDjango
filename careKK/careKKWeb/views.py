from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'careKKWeb/home.html')

def PvsIA(request):
    return render(request,'careKKWeb/PvsIA.html')