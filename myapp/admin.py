from django.contrib import admin
from django.contrib.auth.models import Group, User
# from django import forms
from .models import Product, ProductSubcategory

# Unregister Group and User
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Product)
admin.site.register(ProductSubcategory)
