# Generated by Django 3.2.7 on 2021-09-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='gst',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='organization_name',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]