from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.mylogin, name='mylogin'),
    path('register/', views.myregister, name='myregister'),
    path('panel/', views.panel, name='panel'),

]
