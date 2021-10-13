from django.db import models
from .category import Category
#Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) #cascade is used cause if we delete any category then whole products in that category will also be deleted.
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    discription = models.CharField(max_length=100, default='',null=True, blank=True)
    image = models.ImageField(upload_to='static/images/uploads/')

    def __str__(self):
        return self.name

    #behaviour

    @staticmethod #decorator
    def catch_all_products():
        return Product.objects.all()