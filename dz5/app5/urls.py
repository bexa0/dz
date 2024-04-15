from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/update/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
]
