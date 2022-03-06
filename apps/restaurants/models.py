from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from random import randrange
from uuid import uuid4
from django.template.defaultfilters import slugify

class Restaurant(models.Model):
    restaurant_types =  (
        ('Local', 'Local'),
        ('Japanees', 'Japanees'),
        ('French', 'French'),
    )
    restaurant_name  = models.CharField(max_length=200, unique=True,  null=True, blank=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    ratings = models.ManyToManyField(User, blank=True, related_name="rating")
    restaurant_type = models.CharField(max_length=200, choices=restaurant_types, null=True, blank=True)
    restaurant_image = models.ImageField(upload_to='restaurants', null=True, blank=True)
    restaurant_slug = models.SlugField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "{}".format(self.restaurant_name)
    
    def save(self, *args, **kwargs):
        unique_uuid = str(uuid4()).split("-")[4]
        self.restaurant_slug = slugify("{}".format(unique_uuid))
        super(Restaurant, self).save(*args, **kwargs)
    
    
class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='restaurant', on_delete=models.CASCADE)
    product_name =  models.CharField(max_length=200, null=True, blank=True)
    product_description = models.CharField(max_length=1000, null=True, blank=True)
    product_image = models.ImageField(upload_to="products", null=True, blank=True)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_category = models.ManyToManyField('Category', blank=True, related_name="product_categories")
    product_slug = models.SlugField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return "{}".format(self.product_name)
    
    def save(self, *args, **kwargs):
        unique_uuid = str(uuid4()).split("-")[4]
        self.product_slug = slugify("{}".format(unique_uuid))
        super(Product, self).save(*args, **kwargs)
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, blank=True)
    products = models.ManyToManyField('Product', blank=True, related_name="category_products")
    category_slug = models.SlugField(max_length=200)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return "{}".format(self.category_name)
    
    def save(self, *args, **kwargs):
        unique_uuid = str(uuid4()).split("-")[4]
        self.category_slug = slugify("{}".format(unique_uuid))
        super(Order, self).save(*args, **kwargs)
    
class Order(models.Model):
    product_status = (
        ('Confirmed', 'confirmed'),
        ('Outfordelivery', 'outfordelivery'),
        ('Delivered',  'Delivered'),
        ('NotDelivered',  'NotDelivered')
    )
    payment_methods = (
        ('Online', 'Online'),
        ('CashOndelivery', 'Cashondelivery'),
    )
    payment_status = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    )
    order_id = models.CharField(max_length=200, unique=True)
    restaurants = models.ManyToManyField(Product,  blank=True, related_name="order_restaurants")
    products = models.ManyToManyField(Product,  blank=True, related_name="order_products")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_customer')
    order_status = models.CharField(max_length=200, choices=product_status)
    payment_methods = models.CharField(max_length=200, choices=payment_methods, default="Online")
    payment_status = models.CharField(max_length=200, choices=product_status, default="Unpaid")
    date = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return "order id = {}".format(self.order_id)
    
    def save(self, *args, **kwargs):
        self.order_id = randrange(8)
        super(Order, self).save(*args, **kwargs)