# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishingwall', '0006_auto_20160506_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishing',
            name='wPass',
            field=models.CharField(default=0, max_length=32),
        ),
    ]
