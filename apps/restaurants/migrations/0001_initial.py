# Generated by Django 3.2.12 on 2022-02-24 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=200, null=True)),
                ('category_slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('location', models.CharField(blank=True, max_length=300, null=True)),
                ('restaurant_type', models.CharField(blank=True, choices=[('Local', 'Local'), ('Japanees', 'Japanees'), ('French', 'French')], max_length=200, null=True)),
                ('restaurant_slug', models.SlugField(max_length=200)),
                ('ratings', models.ManyToManyField(blank=True, related_name='rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=200, null=True)),
                ('product_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('product_image', models.ImageField(upload_to='products')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_slug', models.SlugField(max_length=200)),
                ('product_date', models.DateTimeField()),
                ('product_category', models.ManyToManyField(blank=True, related_name='product_categories', to='restaurants.Category')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='restaurants.restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='category_products', to='restaurants.Product'),
        ),
    ]