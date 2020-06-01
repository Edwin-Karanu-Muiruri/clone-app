from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome,),
    path('home/',views.home,),
    path('profile/',views.profile,),
]