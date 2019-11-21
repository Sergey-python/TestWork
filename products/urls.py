from django.urls import path
from .views import *



urlpatterns = [
	path('', list_products, name = 'list_products_url'),
	path('categories/', list_categories, name = 'categories_url'),
	path('categories/<str:product_category>', list_products_in_category, name = 'products_category_url'),
	path('create/', CreatProduct.as_view(), name = 'create_product_url'),
	path('edit/<str:product_name>', EditProduct.as_view(), name = 'edit_product_url'),
	path('delete/<str:product_name>', DeleteProduct.as_view(), name = 'delete_product_url'),
]