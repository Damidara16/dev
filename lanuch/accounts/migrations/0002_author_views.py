# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
