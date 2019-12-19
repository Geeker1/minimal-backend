from django.contrib import admin
from .models import Product, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['available', 'created', 'stock', 'name']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product, ProductAdmin)
