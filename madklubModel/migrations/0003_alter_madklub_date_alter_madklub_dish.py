# Generated by Django 4.0.6 on 2022-08-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madklubModel', '0002_madklub_guests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='madklub',
            name='date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='madklub',
            name='dish',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
