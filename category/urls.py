from django.urls import path
from . import views


urlpatterns = [
    path('panel/create_category/', views.create_category, name='create_category'),
    path('panel/cat_list/', views.category_list, name='category_list'),

]
