from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Resto:
    title = models.CharField(max_length=100, unique=True)
    phone_number = models.DecimalField(max_digits=50)
    address = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='products',
                              null=True,
                              blank=True)








