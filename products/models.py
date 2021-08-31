from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


User = get_user_model()


class Product(models.Model):

    title = models.CharField(max_length=100,)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products',
                              null=True,
                              blank=True)

    liked = models.ManyToManyField(User, default=None, blank=True, related_name='Liked')
    updated = models.DateTimeField(auto_new=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return str(self.title)
    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    products = models.ForeignKey(Products, on_delete = models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.products)

    class Meta:
        ordering = ['title', 'price']

    def __str__(self):
        return self.title


class ProductReview(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='reviews')
    text = models.TextField()
    rating = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


# git init
# git brahcn git checkout master git stash git pull origin master git stash apply  git checkout gulburak git status git add .  git commit -m 'nazvanie commit'git status git push


