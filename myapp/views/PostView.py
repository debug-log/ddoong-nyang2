# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.models.FoodInfo import FoodInfo
from myapp.models.RestaurantInfo import RestaurantInfo
from django.http import JsonResponse
import json

def add_food(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data = json.loads(data)

        restInfo = RestaurantInfo.objects.get(pk=data['restid'])
        new_Food = FoodInfo(restId = restInfo,
            name = data['name'],
            price = data['price'],
            category_big = data['category_big'],
            category_middle = data['category_middle'],
            category_small = data['category_small'])
        new_Food.save()
        return JsonResponse({"created" : data}, safe = False)
    
