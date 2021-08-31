# from django.db import models
#
# from resto.models import Product
#
#
# from resto.models import Product
#
# STATUS_CHOICES = (
#     ('in_progress', 'v obrabotke'),
#     ('finished', 'zaversheni'),
# )
#
# class Order(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     address = models.CharField(max_length=250)
#     paid = models.BooleanField(default=False)
#     title = models.CharField(max_length=100)
#     total_sum = models.DecimalField(max_digits=10,
#                                     decimal_places=2,
#                                     default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)
#     # products = models.ManyToManyField(Products,
#     #                                   through='OrderItem')
#     # resto = models.ForeignKey(Resto,
#                               on_delete = models.RESTRICT,
#                               related_name='')
#     delivery = models.Charfield()
#     class Meta:
#         db_table = 'order'
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
#
#     def __str__(self):
#         return 'Order {}'.format(self.id)
#
#     def get_total_cost(self):
#         return sum(item.get_cost() for item in self.items.all())
#
#
# class OrderItem(models.Model):
#         order = models.ForeignKey(Order,
#                                   on_delete=models.RESTRICT,
#                                   related_name='items')
#         product = models.ForeignKey(Products,
#                                     on_delete=models.RESTRICT,
#                                     related_name='order_items')
#         rice = models.DecimalField(max_digits=10, decimal_places=2)
#         quantity = models.PositiveSmallIntegerField(default=1)
#
#         def __str__(self):
#             return '{}'.format(self.id)
#
#         def get_cost(self):
#             return self.price * self.quantity
#
#
#     ('finished', 'zaversheni'),
#
#
# class Order(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     address = models.CharField(max_length=250)
#     paid = models.BooleanField(default=False)
#     title = models.CharField(max_length=100)
#     total_sum = models.DecimalField(max_digits=10,
#                                     decimal_places=2,
#                                     default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)
#     # products = models.ManyToManyField(Products,
#     #                                   through='OrderItem')
#     # resto = models.ForeignKey(Resto,
#                               on_delete = models.RESTRICT,
#                               related_name='')
#     delivery = models.Charfield()
#     class Meta:
#         db_table = 'order'
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
#
#     def __str__(self):
#         return 'Order {}'.format(self.id)
#
#     def get_total_cost(self):
#         return sum(item.get_cost() for item in self.items.all())
#
#
# class OrderItem(models.Model):
#         order = models.ForeignKey(Order,
#                                   on_delete=models.RESTRICT,
#                                   related_name='items')
#         product = models.ForeignKey(Products,
#                                     on_delete=models.RESTRICT,
#                                     related_name='order_items')
#         rice = models.DecimalField(max_digits=10, decimal_places=2)
#         quantity = models.PositiveSmallIntegerField(default=1)
#
#         def __str__(self):
#             return '{}'.format(self.id)
#
#         def get_cost(self):
#             return self.price * self.quantity

# from django.db import models
#
# # from product.models import Product, User
#
# STATUS_CHOICES = (
#     ('open', 'otkritit'),
#     ('in_progress', 'v obrabotke'),
#     ('canceled', 'otmenenni'),
#     ('finished', 'zaversheni'),
# )
#
# class Order(models.Model):
#
#
#     total_sum = models.DecimalField(max_digits=10,
#                                     decimal_places=2,
#                                     default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User,
#                              on_delete=models.RESTRICT,
#                              related_name='orders'),
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)
#     products = models.ManyToManyField(Product,
#                                       through='OrderItem')
#     class Meta:
#         db_table = 'order'
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order,
#                               on_delete=models.RESTRICT,
#                               related_name='items')
#     product = models.ForeignKey(Product,
#                                on_delete= models.RESTRICT,
#                                related_name='order_items')
#     quantity = models.PositiveSmallIntegerField(default=1)
#     class Meta:
#         db_table = 'order_items'

