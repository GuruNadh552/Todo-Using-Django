from django.shortcuts import render,HttpResponse,redirect
from .models import *
import random as r

# Create your views here.

def index(request):
    todos = ToDoList.objects.all()
    return  render(request,'index.html',{'data':todos})

def addtodo(request):
    if(request.method=='POST'):
        tname = request.POST['todoinp']
        tid = r.randint(0,100)
        data = ToDoList(id = tid,task = tname)
        data.save()
    return  redirect('index')

def deltodo(request,tid):
    data = ToDoList.objects.get(id=tid)
    data.delete()
    return redirect('index')