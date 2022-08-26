# Generated by Django 4.0.6 on 2022-08-20 15:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('madklubModel', '0005_alter_madklub_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='madklub',
            name='participants',
        ),
        migrations.AddField(
            model_name='madklub',
            name='meat_participants',
            field=models.ManyToManyField(blank=True, related_name='meat_participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='madklub',
            name='vegan_participants',
            field=models.ManyToManyField(blank=True, related_name='vegan_participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='madklub',
            name='vegetarian_participants',
            field=models.ManyToManyField(blank=True, related_name='vegetarian_participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
