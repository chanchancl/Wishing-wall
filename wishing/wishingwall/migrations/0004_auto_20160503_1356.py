# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 05:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wishingwall', '0003_wishing_wdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishing',
            name='wData',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 5, 3, 5, 56, 6, 669822, tzinfo=utc)),
        ),
    ]
