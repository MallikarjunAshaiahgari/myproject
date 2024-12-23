from django.shortcuts import render

# Create your views here.

def home(request):
    a='This is Home Page'
    return render(request, 'home.html',context={'data':a})


def create(request):
    data="this is create view"
    return render(request,'create.html',{'data':data})

def delete(request):
    data="this is delete view"
    return render(request,'delete.html',{'data':data})

def edit(request):
    data="this is edit view"
    return render(request,'edit.html',{'data':data})
