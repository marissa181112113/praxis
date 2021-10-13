from django.urls import path
from . import views
# from . import task

urlpatterns = [
    path('', views.index),
    path('<id>/delete', views.delete),
    
]