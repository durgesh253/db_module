# your_app/urls.py
from django.urls import path
from .views import add_product,product_subcategory_list,add_product_subcategory,delete_product_subcategory,update_product_subcategory
urlpatterns = [
    path('', add_product, name='add_product'),
    path('add_product_subcategory',add_product_subcategory, name='add_product_subcategory'),
    path('product_subcategory_list/',product_subcategory_list , name='product_subcategory_list'),
     path('delete_product_subcategory/<int:product_subcategory_id>/', delete_product_subcategory, name='delete_product_subcategory'),
     path('update_product_subcategory/<int:product_subcategory_id>/',update_product_subcategory, name="update_product_subcategory"),
    # Add other URL patterns as needed
]
