from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product

User = get_user_model()

STATUS_CHOICES = (
    ('open', 'open'),
    ('in_progress', 'in_progress'),
    ('done', 'done')
)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,
                             on_delete=models.RESTRICT,
                             related_name='orders')
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='open')
    products = models.ManyToManyField(Product,
                                      through='OrderItem')
