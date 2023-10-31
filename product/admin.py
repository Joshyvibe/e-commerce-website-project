from django.contrib import admin

from .models import Product, Category, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
