# Generated by Django 5.0.4 on 2024-05-22 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_book_list_book_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
