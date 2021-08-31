from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=100,)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products',
                              null=True,
                              blank=True)
    likes = models.DecimalField(max_digits=10, decimal_places=0, null=True)

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
from rest_framework import serializers
from .models import Product, ProductReview


# class ProductSerializer(serializers.Models):
#     class Meta:
#         model = Product
#         fields = ('id', 'body', 'total_likes')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price')


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'image')


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('Цена не может быть отрицательной')
        return price


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'image')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProductReview
        fields = ('id', 'author', 'product', 'text', 'rating', 'created_at')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)
