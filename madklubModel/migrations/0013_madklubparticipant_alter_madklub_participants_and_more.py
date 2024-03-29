# Generated by Django 4.0.6 on 2022-08-23 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyUser', '0001_initial'),
        ('madklubModel', '0012_madklub_participant_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MadklubParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guests', models.PositiveSmallIntegerField(default=0)),
                ('diet', models.CharField(choices=[('vegan', 'Vegan'), ('vegetarian', 'Vegetarian'), ('meat', 'Meat')], default='vegetarian', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='madklub',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', through='madklubModel.MadklubParticipant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Madklub_Participant',
        ),
        migrations.AddField(
            model_name='madklubparticipant',
            name='madklub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='madklub', to='madklubModel.madklub'),
        ),
        migrations.AddField(
            model_name='madklubparticipant',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to=settings.AUTH_USER_MODEL),
        ),
    ]
