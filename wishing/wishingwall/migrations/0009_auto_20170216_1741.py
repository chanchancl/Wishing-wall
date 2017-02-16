# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wishingwall', '0008_serverdata_totalvisit'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipAddress', models.CharField(default='', max_length=32)),
                ('userAgent', models.CharField(default='', max_length=256)),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='serverdata',
            name='totalVisit',
            field=models.IntegerField(verbose_name=0),
        ),
        migrations.AlterField(
            model_name='serverdata',
            name='totalWishing',
            field=models.IntegerField(verbose_name=0),
        ),
    ]
