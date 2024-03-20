from django.db import models

# Create your models here.
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="products/",null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    price = models.FloatField()
    location = models.TextField(max_length=30)
    ingredians = models.TextField(max_length=50)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to="",null=True)
