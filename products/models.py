from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Restaurant(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)

    class Meta:
        ordering = ['title', 'address']

    def __str__(self):
        return f'{self.title} >>> {self.address}'


class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant,
                                   on_delete=models.CASCADE,
                                   related_name='products')
    title = models.CharField(max_length=100,)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products',
                              null=True,
                              blank=True)

    class Meta:
        ordering = ['title', 'price']

    def __str__(self):
        return self.title

    # @property
    # def total_likes(self):
    #     return self.likes.count()


class ProductReview(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} >>> {self.text}'


LIKE_CHOICES = (
    ('like', 'like'),
    ('dislike', 'dislike'),
)


class Like(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             )
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                )
    value = models.CharField(choices=LIKE_CHOICES,
                             default=None,
                             max_length=10)

    def __str__(self):
        return f'{self.product} has {self.value} from {self.user}'


class Favourite(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='favourites')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='favourites')
    is_favourite = models.BooleanField(default=False)

    class Meta:
        pass

    def __str__(self):
        if self.is_favourite:
            return f'{self.user} >>> {self.product} '
