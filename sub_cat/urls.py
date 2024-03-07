from django.urls import path
from . import views


urlpatterns = [
    path('panel/create_subcategory/', views.create_subcat, name='create_subcat'),
    path('panel/subcat_list/', views.subcat_list, name='subcat_list'),

]
