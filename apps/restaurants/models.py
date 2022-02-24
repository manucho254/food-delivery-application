from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

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
    restaurant_slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return "{}".format(self.restaurant_name)
    
    
class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='restaurant', on_delete=models.CASCADE)
    product_name =  models.CharField(max_length=200, null=True, blank=True)
    product_description = models.CharField(max_length=1000, null=True, blank=True)
    product_image = models.ImageField(upload_to="products")
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_category = models.ManyToManyField('Category', blank=True, related_name="product_categories")
    product_slug = models.SlugField(max_length=200)
    product_date = models.DateTimeField()
    
    def __str__(self):
        return "{}".format(self.product_name)
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, blank=True)
    products = models.ManyToManyField('Product', blank=True, related_name="category_products")
    category_slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return "{}".format(self.category_name)