from django.urls import path
from . import views

urlpatterns = [
    path('products_list/', views.prod_list, name='prod_list'),
    path('products_list/products_new/', views.prod_new, name='prod_new'),
    path('products_list/details/<int:pk>/', views.prod_details, name='prod_details'),
    path('products_list/update/<int:pk>/', views.prod_update, name='prod_update'),
    path('products_list/delete/<int:pk>', views.prod_delete, name='prod_delete'),
]