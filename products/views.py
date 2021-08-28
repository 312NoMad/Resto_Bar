from django.http import HttpResponse

from django.shortcuts import render
from rest_framework import viewsets, mixins

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from product.models import Product, ProductReview
from product.permissions import IsAuthorOrIsAdmin
from product.serializers import (ProductSerializer, ProductDetailsSerializer, CreateProductSerializer, ReviewSerializer)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
def test_view(request):
    return HttpResponse('hello world')
class ProductFilter(filters.FilterSet):
    price_from = filters.NumberFilter('price', 'gte')
    price_to = filters.NumberFilter('price', 'lte')

    class Meta:
        model = Products
        fields = ('price_from', 'price_to')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [filters.DjangoFilterBackend, rest_filters.SearchFilter, rest_filters.OrderingFilter]

    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'price']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        elif self.action == 'retrieve':
            return ProductDetailsSerializer
        return CreateProductSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return []

    @action(['GET'], detail=True)
    def reviews(self, request, pk=None):
        product = self.get_object()

        reviews = product.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=200)
class ReviewViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAuthorOrIsAdmin()]
        return []

