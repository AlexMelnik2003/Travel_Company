# Generated by Django 5.0.6 on 2024-05-23 12:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_profile_email_remove_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiration_date',
            field=models.CharField(max_length=5, validators=[django.core.validators.MinValueValidator(2023)]),
        ),
    ]