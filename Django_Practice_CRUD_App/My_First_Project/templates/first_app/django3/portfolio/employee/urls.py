
from django.urls import path,include
from . import views

urlpatterns = [

    path('new/',views.employee),
    path('profile/',views.profile),


]
