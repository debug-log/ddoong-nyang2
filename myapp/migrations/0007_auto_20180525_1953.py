# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-25 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_user_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dietinfo',
            options={'ordering': ('types',)},
        ),
        migrations.RemoveField(
            model_name='dietinfo',
            name='date',
        ),
        migrations.AddField(
            model_name='dietinfo',
            name='day',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='foodinfo',
            name='category_big',
            field=models.CharField(choices=[('양식', '양식'), ('한식', '한식'), ('일식', '일식'), ('중식', '중식'), ('동남아', '동남아'), ('분식', '분식')], max_length=20),
        ),
    ]
