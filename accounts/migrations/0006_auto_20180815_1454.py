# Generated by Django 2.1 on 2018-08-15 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180815_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='please change', max_length=255, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
