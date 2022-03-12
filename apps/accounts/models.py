from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
from django.template.defaultfilters import slugify
from uuid import uuid4
from django.contrib.auth.models import AbstractBaseUser,AbstractUser

phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class User(AbstractUser):
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=17, default="+254", validators=[phone_regex], blank=True, unique=True, help_text="format: +254706485732 start with your country code")
    otp = models.CharField(max_length=66)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    
class Profile(models.Model):
    profile_user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='profile_user')
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    profile_slug = models.SlugField(max_length=200)
    date  = models.DateField(default=timezone.now)
    
    def __str__(self):
        return "{}".format(self.username)
    
    def save(self,  *args, **kwargs):
        unique_uuid = uuid4()
        self.profile_slug = slugify("{}".format(unique_uuid))
        super(Profile, self).save(*args, **kwargs)

