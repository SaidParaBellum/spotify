# Generated by Django 5.1 on 2024-08-31 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='musician')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('role', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('duration', models.IntegerField()),
                ('file', models.FileField(upload_to='songs')),
                ('cover', models.ImageField(upload_to='songs')),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sporify.musician')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('longetivity', models.DateTimeField()),
                ('songs', models.ManyToManyField(related_name='playlist', to='sporify.song')),
                ('user', models.ManyToManyField(related_name='playlist', to='sporify.user')),
            ],
        ),
        migrations.AddField(
            model_name='musician',
            name='user',
            field=models.ManyToManyField(related_name='musician', to='sporify.user'),
        ),
    ]
