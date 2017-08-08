# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 09:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import prenovi.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('prenovi', '0003_auto_20170721_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('work', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='WorkInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(default=datetime.datetime(2017, 7, 30, 11, 50, 57, 194458))),
                ('end_date', models.DateTimeField(default=prenovi.models.get_end_date)),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prenovi.Contractor')),
            ],
        ),
    ]