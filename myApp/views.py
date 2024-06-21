from django.http import HttpResponse
from django.shortcuts import render
from myApp.models import information

# Create your views here.

def index(request):
    return render(request, 'index.html')

def display(request):
    data=information.objects.all()
    return render(request, 'display.html',{'user':data})

def submitdata(request):
    a = request.POST.get('fname')
    b = request.POST.get('lname')
    c = request.POST.get('email')
    
    object = information(firstname = a,lastname = b,email = c)
    object.save()
    
    return HttpResponse("Data submit succesfully")