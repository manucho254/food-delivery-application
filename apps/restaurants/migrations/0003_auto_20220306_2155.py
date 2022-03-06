# Generated by Django 3.2.12 on 2022-03-06 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_customer', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default=True, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Confirmed', 'confirmed'), ('Outfordelivery', 'outfordelivery'), ('Delivered', 'Delivered'), ('NotDelivered', 'NotDelivered')], default=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_methods',
            field=models.CharField(choices=[('Online', 'Online'), ('CashOndelivery', 'Cashondelivery')], default='Online', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('Confirmed', 'confirmed'), ('Outfordelivery', 'outfordelivery'), ('Delivered', 'Delivered'), ('NotDelivered', 'NotDelivered')], default='Unpaid', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='restaurants',
            field=models.ManyToManyField(blank=True, related_name='order_restaurants', to='restaurants.Product'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='restaurant_image',
            field=models.ImageField(blank=True, null=True, upload_to='restaurants'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='order_products', to='restaurants.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]