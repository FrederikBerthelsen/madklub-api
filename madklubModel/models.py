from django.db import models
from django.contrib.postgres.fields import ArrayField
from MyUser.models import MyUser

DIET_OPTIONS = (
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('meat', 'Meat')
    )

class Madklub(models.Model):
    owner = models.ForeignKey(MyUser, null=False, blank=False, on_delete=models.CASCADE)
    dish = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=False, blank=False, unique=True)
    active = models.BooleanField(default=True)
    participants = models.ManyToManyField(MyUser, blank=True, related_name="participants", through="MadklubParticipant")
    diet = ArrayField(
        models.CharField(choices=DIET_OPTIONS, max_length=10, default="vegetarian")
    )
    
    class Meta:
        ordering = ('date',)

class MadklubParticipant(models.Model):
    participant = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    madklub = models.ForeignKey(Madklub, on_delete=models.CASCADE)
    guests = models.PositiveSmallIntegerField(default=0)
    diet = models.CharField(choices=DIET_OPTIONS, max_length=10, default="vegetarian")
