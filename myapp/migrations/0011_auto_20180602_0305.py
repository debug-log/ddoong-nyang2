# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-01 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20180531_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='button',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_request',
            field=models.IntegerField(default=0),
        ),
    ]
