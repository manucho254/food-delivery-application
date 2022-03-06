from django.contrib import admin
from .models import *

admin.site.register(Restaurant)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)