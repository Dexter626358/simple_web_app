from django.urls import path

from . import views

urlpatterns = [
 path('', views.welcome_view, name='index'),
 path('contacts/', views.contacts, name='contacts'),
 path('order_call/', views.order_call, name='order_call'),
 path('product_list/', views.product_list, name='products'),
]
