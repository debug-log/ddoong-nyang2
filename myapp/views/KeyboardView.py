# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.models import *
from django.http import JsonResponse
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist

from .decorators import bot
import json, random
import datetime


t = Button.objects.annotate(mod = F('button_id')%1000).filter(mod = 0)
buttons = [item.button_name for item in t]

category_big_list = [x[0] for x in FoodInfo.CATEGORY_BIG]
category_middle_list = [x[0] for x in FoodInfo.CATEGORY_MIDDLE]
category_small_list = [x[0] for x in FoodInfo.CATEGORY_SMALL if x[0] is not 'NONE']

button_diet_info = ['오늘의 건강한 식단', '오늘의 건강한 운동 방법']

def user_append_content(user, content):
    if not user.content:
        user.content = content
    else:
        user.content += (',' + content)
    user.save()

def depth_button(text, btns):
    if len(btns) == 0:
        btns = buttons

    return {
        'message' : {
                'text' : text
            },
        'keyboard' : {
            'type' : 'buttons',
            'buttons' : btns
        }
    }

def recommend_food(content):
    params = content.split(',')
    if len(params) < 2:
        return '해당하는 음식이 없습니다.'
    elif len(params) == 2:
        entry = FoodInfo.objects.filter(category_big = params[0], category_middle = params[1])
    elif len(params) == 3:
        entry = FoodInfo.objects.filter(category_big = params[0], category_middle = params[1], category_small = params[2])
    
    count = entry.count()
    randIndex = random.randrange(count)
    food = entry[randIndex]

    rest_name = food.restId.name
    rest = RestaurantInfo.objects.get(pk = rest_name)

    ret1 = """오늘의 추천식단은
[{0}]!!

가격은 {1}원이고, {2}에서 사먹을 수 있다냥!

평일 운영시간은
{3}
이고,

""".format(food.name, food.price, rest.name, rest.text_date_day)

    if rest.text_date_holiday == '.':
        ret2 = "휴일에는 운영하지 않는 다냥"
    else:
        ret2 = """휴일 운영시간은
{0}
이다냥!""".format(rest.text_date_holiday)

    return ret1 + ret2


def not_yet():
    return {
        'message' : {
            'text' : '아직 준비 중입니다냥.'
        },
        'keyboard' : {
            'type' : 'buttons',
            'buttons' : buttons
        }
    }

def diet_info(info):
    return {
        'message' : {
            'text' : info.text,
            'photo' : {
                'url' : info.photo_url,
                'width' : 640,
                'height' : 480
            },
            'message_button' : {
                'label' : info.button_label,
                'url' : info.button_url,
            },
        },
        'keyboard' : {
            'type' : 'buttons',
            'buttons' : buttons
        }
    }

clinic_info = {
    'message' : {
        'text' : """잘 생각했다냥!
뚱냥이보다 잘 하는 닝겐이 있는데 소개시켜줄테니 한 번 찾아 가보라냥!~!""",
        
        'message_button' : {
            'label' : '백병원식이장애클리닉',
            'url' : 'http://www.paik.ac.kr/bh/da/jin/eatingclinic/sub01.htm'
        },
    },
    'keyboard' : {
        'type' : 'buttons',
        'buttons' : buttons
    }
}


@bot
def on_init(request):
    return {
        'type' : 'buttons',
        'buttons' : buttons
    }

@bot
def on_message(request):
    user_key = 'kakao-' + request.JSON['user_key']
    types = request.JSON['type']
    content = request.JSON['content']

    user = User.objects.get_or_create(name = user_key)[0]
    try:
        button = Button.objects.get(button_name = content)
        button_type = button.button_id // 1000

        user.last_request = button.button_id
        user.save()
    
    except ObjectDoesNotExist:
        return not_yet()

    if button_type == 1:
        #do introduce
        pass
    elif button_type == 2:
        #do recommend food
        pass
    elif button_type == 3:
        #do recommend food
        if button.button_id == 3000:
            recommend_food_items = Button.objects.annotate(val = F('button_id')/1000, mod = F('button_id')%1000).filter(val = 3).exclude(mod = 0)
            recommend_food_buttons = [item.button_name for item in recommend_food_items]
            return depth_button(button.text, recommend_food_buttons)

        today = datetime.datetime.today().weekday()
        if button.button_id == 3100:
            return diet_info(DietInfo.objects.filter(types = '식단', day = today)[0])

        elif button.button_id == 3200:
            return diet_info(DietInfo.objects.filter(types = '운동', day = today)[0])
        else:
            pass
    elif button_type == 4:
        #do recommend food
        pass
    elif button_type == 5:
        #do recommend food
        pass
    elif button_type == 6:
        #do recommend food
        pass
    elif button_type == 7:
        #do recommend food
        pass
    else:
        return not_yet()

    return depth_button(button.text, buttons)

    if (content in buttons) and (user.last_request is not content):
        user.last_request = content
        user.content = ''
        user.save()

    if '식단좀 추천 해주라' in content:
        return depth_button('어떤 종류의 음식이 먹고 싶냥?', category_big_list)
    elif content in category_big_list:
        user_append_content(user, content)

        entry = FoodInfo.objects.filter(category_big = content)
        next_food_list = list(set(entry.values_list('category_middle', flat=True)))

        return depth_button('다양한 음식들이 마련되어 있다냥!', next_food_list)
    elif content in category_middle_list:
        user_append_content(user, content)

        if content in ['스파게티', '그라탕']:
            entry = FoodInfo.objects.filter(category_middle = content)
            next_food_list = list(set(entry.values_list('category_small', flat=True)))
            if 'NONE' in next_food_list:
                next_food_list.remove('NONE')

            return depth_button('어떤 소스를 원하냥!!?', next_food_list)
        else:
            return depth_button(recommend_food(user.content), buttons)
    elif content in category_small_list:
        user_append_content(user, content)

        return depth_button(recommend_food(user.content), buttons)


    elif '건강한 식습관,운동 정보가 필요해' in content:
        return depth_button('어떤 정보를 알려줄까냥? 요일마다 다른 정보를 알려주겠다냥!', button_diet_info)
    elif content in button_diet_info:
        if '식단' in content:
            today = datetime.datetime.today().weekday()
            return diet_info(DietInfo.objects.filter(types = '식단', day = today)[0])
        else:
            today = datetime.datetime.today().weekday()
            return diet_info(DietInfo.objects.filter(types = '운동', day = today)[0])


    elif '병원' in content:
        return clinic_info
    else:
        return not_yet()

@bot
def on_added(request):
	pass

@bot
def on_block(request):
	if request.method == 'DELETE':
		pass
@bot
def on_leave(request):
	if request.method == 'DELETE':
		pass