from django.db import models

# Create your models here.
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="product/",null=True)

    def __str__(self):
        return self.name
