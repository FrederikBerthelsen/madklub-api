from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from MyUser.models import MyUser

class Schema(models.Model):
    week = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(53)])
    users = models.ManyToManyField(MyUser, related_name="users")

    class Meta:
        ordering = ('week',)
