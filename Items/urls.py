from django.urls import path
from . import views


urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart/delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('item/<str:position>/', views.item_detail, name='item_detail'),
    path('add_to_cart/<str:position>/', views.add_to_cart, name='add_to_cart'),
    path('check_out/', views.check_out, name='check_out'),
    path('Buy_now/', views.buy_now_check_out, name='buy_now_check_out'),

]
