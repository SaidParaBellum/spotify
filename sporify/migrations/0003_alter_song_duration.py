# Generated by Django 5.1 on 2024-08-31 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sporify', '0002_musician_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.CharField(max_length=5),
        ),
    ]
