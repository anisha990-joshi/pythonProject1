# Generated by Django 3.2.9 on 2021-11-20 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epic', '0018_auto_20211120_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cover',
            new_name='Image',
        ),
    ]
