# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-13 16:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 14, 16, 17, 29, 137640, tzinfo=utc)),
        ),
    ]
