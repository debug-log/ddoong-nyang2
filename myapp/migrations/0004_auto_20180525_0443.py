# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-24 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20180524_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodinfo',
            name='category_big',
            field=models.CharField(choices=[('양식', '양식'), ('한식', '한식'), ('일식', '일식'), ('중식', '중식'), ('퓨전', '퓨전'), ('동남아', '동남아'), ('분식', '분식')], max_length=20),
        ),
        migrations.AlterField(
            model_name='foodinfo',
            name='category_middle',
            field=models.CharField(choices=[('국/탕', '국/탕'), ('그라탕', '그라탕'), ('김밥', '김밥'), ('랩', '랩'), ('면', '면'), ('밥', '밥'), ('버거', '버거'), ('분식', '분식'), ('브리또', '브리또'), ('빵', '빵'), ('샌드위치', '샌드위치'), ('샐러드', '샐러드'), ('샐러드버거세트', '샐러드버거세트'), ('세트', '세트'), ('스파게티', '스파게티'), ('스프', '스프'), ('요리', '요리'), ('웜볼', '웜볼'), ('정식', '정식'), ('찜', '찜'), ('치킨', '치킨'), ('탕수육', '탕수육'), ('피자', '피자'), ('기타', '기타')], max_length=20),
        ),
        migrations.AlterField(
            model_name='foodinfo',
            name='category_small',
            field=models.CharField(choices=[('NONE', 'NONE'), ('토마토', '토마토'), ('크림', '크림'), ('로제', '로제'), ('오일', '오일'), ('기타', '기타')], max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurantinfo',
            name='text_date_holiday',
            field=models.TextField(null=True),
        ),
    ]