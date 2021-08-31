from django.urls import path
from .views import post_view

app_name = 'products'

urlpatterns = [
    path('', post_view, name='post-list')
]