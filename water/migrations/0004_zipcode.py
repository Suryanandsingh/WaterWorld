# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_code', models.CharField(default=111111, max_length=6)),
            ],
        ),
    ]
