# Generated by Django 5.0.6 on 2024-05-25 10:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_payment_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(16)]),
        ),
    ]
