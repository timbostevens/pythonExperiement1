# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 10:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snesgame',
            name='display',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='snesgame',
            name='releaseDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
