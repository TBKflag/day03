# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180428_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]