# Generated by Django 3.2 on 2021-09-02 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_product_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='value',
        ),
        migrations.AddField(
            model_name='like',
            name='liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='like',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='products.product'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]