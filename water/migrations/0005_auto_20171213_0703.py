# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-13 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0004_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_logo',
            field=models.FileField(upload_to=b''),
        ),
    ]