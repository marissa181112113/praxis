from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('<id>/delete', views.delete),
    
]
