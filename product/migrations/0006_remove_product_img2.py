# Generated by Django 3.2.7 on 2021-09-07 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210906_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img2',
        ),
    ]
