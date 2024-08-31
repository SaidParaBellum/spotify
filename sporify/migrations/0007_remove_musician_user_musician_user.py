# Generated by Django 5.1 on 2024-08-31 18:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sporify', '0006_alter_user_date_of_birth_alter_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='user',
        ),
        migrations.AddField(
            model_name='musician',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='musician', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]