from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models


# from . import task

# Create your views here.
def index (request):
    if request.POST:
        models.makanan.objects.create(
            itemmakan=request.POST['itemmakan'], 
            jenismakan=request.POST['jenismakan'], 
            jumlahmakan=request.POST['jumlahmakan'], 
            hargamakan=request.POST['hargamakan'],
            )
       
        models.minuman.objects.create(
             itemminum=request.POST['itemminum'], 
             jenisminum=request.POST['jenisminum'], 
             jumlahminum=request.POST['jumlahminum'], 
             hargaminum=request.POST['hargaminum']
            )
        return redirect('/')
    tasks = models.makanan.objects.all()
    tasks1 = models.minuman.objects.all()
    return render(request, 'index.html', {
    'data' : tasks,
    'data1' : tasks1,
    })
def deletemakan(request, id):
    models.makanan.objects.filter(pk=id).delete()
    return redirect('/')

def rincianmakan(request, id):
    tasks = models.makanan.objects.filter(pk=id).first()
    return render(request,'rincian.html', {
    'data': tasks,
    })
def editmakan(request, id) :
    if request.POST:
        models.makanan.objects.filter(pk=id).update(
                itemmakan=request.POST['itemmakan'], 
                jenismakan=request.POST['jenismakan'], 
                jumlahmakan=request.POST['jumlahmakan'], 
                hargamakan=request.POST['hargamakan'])
        return redirect('/')

    tasks = models.makanan.objects.all()
    return render(request, 'edit.html', {
    'data': tasks,
    })
def deleteminum(request, id):
     models.minuman.objects.filter(pk=id).delete()
     return redirect('/')

def rincianminum(request, id):
     tasks1 = models.minuman.objects.filter(pk=id).first()
     return render(request,'rincian.html', {
    'data' : tasks1,
     } )
def editminum(request, id) :
    if request.POST:
        models.minuman.objects.filter(pk=id).update(
                itemminum=request.POST['itemminum'], 
                jenisminum=request.POST['jenisminum'], 
                jumlahminum=request.POST['jumlahminum'], 
                hargaminum=request.POST['hargaminum'])
        return redirect('/')

    tasks1 = models.minuman.objects.all()
    return render(request, 'edit.html', {
    'data': tasks1,
    })

# def index (request):
#      if request.POST:
#          models.minuman.objects.create(
#              itemminum=request.POST['itemminum'], 
#              jenisminum=request.POST['jenisminum'], 
#              jumlahminum=request.POST['jumlahminum'], 
#              hargaminum=request.POST['hargaminum'])
#          return redirect('/')
#      tasks = models.minuman.objects.all()
#      return render(request, 'index.html', {
#      'data' : tasks,
#      })

