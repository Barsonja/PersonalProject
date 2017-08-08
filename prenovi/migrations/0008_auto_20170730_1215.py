# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 10:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenovi', '0007_auto_20170730_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workinstance',
            name='client_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workinstance',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 30, 12, 15, 39, 271410)),
        ),
        migrations.AlterField(
            model_name='workinstance',
            name='summary',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='workinstance',
            name='title',
            field=models.CharField(help_text='Name of the project', max_length=100),
        ),
    ]