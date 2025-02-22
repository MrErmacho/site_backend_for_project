from django.db import models

from core.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/Product/')
    desc = models.TextField()
    price = models.FloatField()
    discount = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField()
    stock = models.PositiveIntegerField() # в наличии кол-во
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name






class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    delivery_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


