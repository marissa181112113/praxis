from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models

# Create your views here.
def index (request):
    if request.POST:
        models.makanan.objects.create(
            itemmakan=request.POST['itemmakan'], 
            jenismakan=request.POST['jenismakan'], 
            jumlahmakan=request.POST['jumlahmakan'], 
            hargamakan=request.POST['hargamakan'])
        return redirect('/')
    tasks = models.makanan.objects.all()
    return render(request, 'index.html', {
    'data' : tasks,
    })
def delete(request, id):
    models.makanan.objects.filter(pk=id).delete()
    return redirect('/')

def rincian(request, id):
    models.makanan.objects.filter(pk=id).first()
    return redirect('/')

# def index (request):
#     if request.POST:
#         models.minuman.objects.create(
#             itemminum=request.POST['itemminum'], 
#             jenisminum=request.POST['jenisminum'], 
#             jumlahminum=request.POST['jumlahminum'], 
#             hargaminum=request.POST['hargaminum'])
#         return redirect('/')
#     tasks = models.minuman.objects.all()
#     return render(request, 'index.html', {
#     'data' : tasks,
#     })

# def delete(request, id):
#     models.minuman.objects.filter(pk=id).delete()
#     return redirect('/')

# def rincian(request, id):
#     models.minuman.objects.filter(pk=id).first()
#     return redirect('/')