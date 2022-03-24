# Generated by Django 2.2.26 on 2022-03-24 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('likes', models.IntegerField(default=0)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('likers', models.ManyToManyField(blank=True, default=None, related_name='Likers', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=15)),
                ('surname', models.CharField(blank=True, max_length=15)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=15)),
                ('surname', models.CharField(blank=True, max_length=15)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(blank=True, max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagenest.Image')),
                ('likers', models.ManyToManyField(related_name='favorites', to='imagenest.UserProfile')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagenest.UserProfile')),
            ],
            options={
                'ordering': ['-creation_time'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagenest.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
