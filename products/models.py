from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    resto = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products',
                              null=True,
                              blank=True)
    def __str__(self):
        return self.title


class Products:
    pass


class ProductReview(models.Model):
    products = models.ForeignKey(Products,
                              on_delete=models.CASCADE,
                              related_name = 'reviews')
    author = models.ForeignKey(User,
                               on_delete = models.CASCADE,
                               related_name = 'reviews')
    text = models.TextField()
    rating = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_new_add=True)



