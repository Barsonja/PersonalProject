# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 12:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenovi', '0013_auto_20170730_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workinstance',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 30, 14, 19, 38, 49657)),
        ),
    ]