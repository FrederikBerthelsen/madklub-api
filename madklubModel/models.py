from django.db import models
from django.contrib.postgres.fields import ArrayField
from MyUser.models import MyUser

DIET_OPTIONS = (
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('meat', 'Meat')
    )

class Madklub(models.Model):
    owner = models.ForeignKey(MyUser, related_name="owner", on_delete=models.CASCADE)
    dish = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=False, blank=False, unique=True)
    guests = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    participants = models.ManyToManyField(MyUser, related_name="participants", blank=True)
    diet = ArrayField(
        models.CharField(choices=DIET_OPTIONS, max_length=10, default="vegetarian")
    )
