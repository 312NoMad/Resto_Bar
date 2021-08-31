# from django.db import models
#
# from django.db.models import ForeignKey
# from django.contrib.auth.models import User, Product
#
# class Preference(models.Model):
#     likes = models.ManyToManyField(User, Product, related_name = 'bloglikes')
#     user = models.ForeignKey(User)
#     product = models.ForeignKey(Product)
#     value = models.BooleanField(default=False)
#     date = models.DateTimeField(auto_new=True)
#     def __str__(self):
#         return str(self.user) + ':' + str(self.product)
#     # class Meta:
#     #     unique_together = ('user', 'product', 'value')
#     def number_of_likes(self):
#         return self.likes.count()
from django.db import models
from django.contrib.auth.models import User, Products

# class Products(models.Model):
#     title = models.CharField(max_length = 150)
#     body = models.TextField()
#     liked = models.ManyToManyField(User, default=None, blank = True, related_name='liked')
#     updated = models.DateTimeField(auto_new=True)
#     created = models.DateTimeField(auto_new=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'author')
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ForeignKey(Likes, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default = 'Like', max_length=10)
    likes = models.ManyToManyField(User, Products, related_name = 'bloglikes')
    user = models.ForeignKey(User)
    product = models.ForeignKey(Products)

    def __str__(self):
        return str(self.title)
    @property
    def num_likes(self):
        return self.liked.all().count
    def __str__(self):
        return str(self.post)







