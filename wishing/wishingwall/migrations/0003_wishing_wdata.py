# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 05:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wishingwall', '0002_serverdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishing',
            name='wData',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 3, 5, 54, 32, 250605, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
