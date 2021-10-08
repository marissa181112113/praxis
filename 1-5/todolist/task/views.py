from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
# Create your views here.

def index(req):
    if req.POST:
        models.Task.objects.create(item=req.POST['item'])
        return redirect('/')

    tasks = models.Task.objects.all()
    return render(req, 'index.html', {
        'data': tasks,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/')

def rincian(req, id):
    models.Task.objects.filter(pk=id).first()
    return redirect('/')
