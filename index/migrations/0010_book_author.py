# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-04 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='index.Author'),
        ),
    ]
