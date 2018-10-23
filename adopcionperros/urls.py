from django.urls import path
from . import views

# REEMPLAZE post_list por index ... !!!
urlpatterns = [
    #path('', views.post_list, name='index'),
    path('', views.index, name='index'),
]

