# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-31 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_button'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodinfo',
            name='category_middle',
            field=models.CharField(choices=[('국/탕', '국/탕'), ('그라탕', '그라탕'), ('김밥', '김밥'), ('떡볶이', '떡볶이'), ('랩', '랩'), ('만두', '만두'), ('면', '면'), ('밥', '밥'), ('버거', '버거'), ('브리또', '브리또'), ('빵', '빵'), ('샌드위치', '샌드위치'), ('샐러드', '샐러드'), ('샐러드버거세트', '샐러드버거세트'), ('세트', '세트'), ('스파게티', '스파게티'), ('스프', '스프'), ('오뎅', '오뎅'), ('요리', '요리'), ('웜볼', '웜볼'), ('정식', '정식'), ('찜', '찜'), ('치킨', '치킨'), ('탕수육', '탕수육'), ('피자', '피자'), ('기타', '기타')], max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_request',
            field=models.IntegerField(null=True),
        ),
    ]
