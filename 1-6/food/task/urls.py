from django.urls import path
from . import views
# from . import task

urlpatterns = [
    path('', views.index),
    path('<id>/delete', views.deletemakan),
    path('<id>/rincian', views.rincianmakan),
    path('<id>/edit', views.editmakan),
    path('minum/<id>/delete', views.deleteminum),
    path('<id>/rincian', views.rincianminum),
    path('<id>/edit', views.editminum),
    
    
]