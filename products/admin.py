from django.contrib import admin

from .models import Product, ProductReview, Like, Restaurant, Favourite

admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(Like)
admin.site.register(Restaurant)
admin.site.register(Favourite)