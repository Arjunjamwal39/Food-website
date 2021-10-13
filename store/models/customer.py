from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30)
    phoneno = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
    def isexist(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False    