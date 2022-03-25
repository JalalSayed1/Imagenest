# Generated by Django 2.2.26 on 2022-03-25 15:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagenest', '0002_auto_20220325_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='likers',
            field=models.ManyToManyField(related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
