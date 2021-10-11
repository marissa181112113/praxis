from django.http import request
from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index (request) :
    if request.POST :
        models.Task.objects.create(item=request.POST['item'])
        return redirect('/')
    tasks = models.Task.objects.all()
    return render(request, 'index.html', {
    'data' : tasks,
    })
def delete(request, id) :
    models.Task.objects.filter(pk=id).delete()
    return redirect('/')

def rincian(request, id) :
    models.Task.objects.filter(pk=id).first()
    return redirect('/')