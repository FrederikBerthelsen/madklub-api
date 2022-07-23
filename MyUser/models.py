import django
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

from django.utils.translation import gettext_lazy as _

class MyUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    DIET_CHOICES = (
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('meat', 'Meat')
    )

    diet = models.CharField(max_length=10, choices=DIET_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['diet', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
