from django.urls import path

from . import views

urlpatterns = [
    path("january", views.index),   #if request reaches /january, then execute index function
    path("february", views.hello), #if request reaches /january, then execute january function
]

