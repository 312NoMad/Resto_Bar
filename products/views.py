from rest_framework import viewsets, mixins

from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from .models import Product, ProductReview
from .serializers import ProductSerializer, CreateProductSerializer, ProductDetailsSerializer, ReviewSerializer
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product, Like
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [filters.DjangoFilterBackend,
                       rest_filters.SearchFilter,
                       rest_filters.OrderingFilter]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        elif self.action == 'retrieve':
            return ProductDetailsSerializer
        return CreateProductSerializer


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ReviewSerializer

def post_view(request):
    queryset = Product.objects.all()
    user = request.user
    context = {
        'queryset': queryset,
        'user': user,
    }
    return render(request)
def like_post(request):
    user = request.user
    if request.method == 'POST':
        products_id = request.POST.get('post_id')
        product_obj = Product.objects.get(id=products_id)

        if user in products_id.liked.all():
            product_obj.liked.remove(user)
        else:
            product_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, products_id=products_id)
        if not created:
            if like.value == 'Like':
               like.value == 'Unlike'
            else:
               like.value = 'Like'
        like.save()




