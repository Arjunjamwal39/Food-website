from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Register your models here.

class showtable(admin.ModelAdmin):
    list_display=['name','price','category']

class Customersadmin(admin.ModelAdmin):
    list_display = ("name","phoneno","email",'password')
admin.site.register(Customer, Customersadmin)

admin.site.register(Product, showtable)
admin.site.register(Category)


