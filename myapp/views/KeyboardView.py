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

    if rest.text_date_holiday == '.':
        return TextTable.objects.get(key = 'recommend_food').text.format(food.name, food.price, rest.name, rest.text_date_day)
    else:
        return TextTable.objects.get(key = 'recommend_food_holi').text.format(food.name, food.price, rest.name, rest.text_date_day, rest.text_date_holiday)

def recommend_random_food():
    count = FoodInfo.objects.all().count()
    randIndex = random.randrange(count)
    food = FoodInfo.objects.all()[randIndex]
    rest_name = food.restId.name
    rest = RestaurantInfo.objects.get(pk = rest_name)

    if rest.text_date_holiday == '.':
        return TextTable.objects.get(key = 'recommend_food').text.format(food.name, food.price, rest.name, rest.text_date_day)
    else:
        return TextTable.objects.get(key = 'recommend_food_holi').text.format(food.name, food.price, rest.name, rest.text_date_day, rest.text_date_holiday)


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

def buy_link(text, btns):
    return {
        'message' : {
            'text' : text,
            'photo' : {
                'url' : 'https://lh3.googleusercontent.com/0fLSkaWhPjJFj5EolVTtxqQEF5pLpxT4AmRcMFZxRlFZQr9z6CCmOqoEWZcU5lVRhfKPMAPAQg',
                'width' : 640,
                'height' : 480
            },
            'message_button' : {
                'label' : '구매신청 하러가기',
                'url' : 'https://goo.gl/forms/hLebQrMwDihbfDjs2',
            },
        },
        'keyboard' : {
            'type' : 'buttons',
            'buttons' : btns
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
        if user.last_request == 2101:
            user_append_content(user, content)
            user.last_request = 2102
            user.save()

            entry = FoodInfo.objects.filter(category_big = content)
            next_food_list = list(set(entry.values_list('category_middle', flat=True)))

            return depth_button('다양한 음식들이 마련되어 있다냥!', next_food_list)
        elif user.last_request == 2102:
            user_append_content(user, content)

            if content in ['스파게티', '그라탕']:
                entry = FoodInfo.objects.filter(category_middle = content)
                next_food_list = list(set(entry.values_list('category_small', flat=True)))
                if 'NONE' in next_food_list:
                    next_food_list.remove('NONE')

                return depth_button('어떤 소스를 원하냥!!?', next_food_list)
            else:
                return depth_button(recommend_food(user.content), buttons)
        else:
            return not_yet()

    if button_type == 1:
        #do introduce
        pass
    elif button_type == 2:
        #do recommend food
        if button.button_id == 2000:
            recommend_food_items = Button.objects.annotate(val = F('button_id')/1000, mod = F('button_id')%1000).filter(val = 2).exclude(mod = 0)
            recommend_food_buttons = [item.button_name for item in recommend_food_items]

            user.content = ''
            user.save()
            return depth_button(button.text, recommend_food_buttons)

        if button.button_id == 2100:
            #category
            user.last_request = 2101
            user.save()
            return depth_button('어떤 종류의 음식이 먹고 싶냥?', category_big_list)
        elif button.button_id == 2200:
            #random
            return depth_button(recommend_random_food(), buttons)

    elif button_type == 3:
        #do recommend_diet_info
        if button.button_id == 3000:
            recommend_diet_info_items = Button.objects.annotate(val = F('button_id')/1000, mod = F('button_id')%1000).filter(val = 3).exclude(mod = 0)
            recommend_diet_info_buttons = [item.button_name for item in recommend_diet_info_items]
            return depth_button(button.text, recommend_diet_info_buttons)

        today = datetime.datetime.today().weekday()
        if button.button_id == 3100:
            return diet_info(DietInfo.objects.filter(types = '식단', day = today)[0])

        elif button.button_id == 3200:
            return diet_info(DietInfo.objects.filter(types = '운동', day = today)[0])
        else:
            pass
    elif button_type == 4:
        #do self-test
        if button.button_id == 4000:
            user.test_score = 0
            user.save()
            return depth_button(button.text, [Button.objects.get(button_id = 4100).button_name])

        button_yes_or_no = [Button.objects.get(button_id = 4200).button_name, Button.objects.get(button_id = 4300).button_name]
        
        if button.button_id == 4200:
            user.test_score += 100
            user.save()
        elif button.button_id == 4300:
            user.test_score += 1
            user.save()

        nth = (user.test_score // 100) + (user.test_score % 100) + 1

        if nth == 16:
            answer_yes = (user.test_score // 100)
            if answer_yes <= 2:
                return depth_button(TextTable.objects.get(key = 'test_result_01').text, buttons)
            elif answer_yes <= 5:
                return depth_button(TextTable.objects.get(key = 'test_result_02').text, buttons)
            else:
                return depth_button(TextTable.objects.get(key = 'test_result_03').text, buttons)               

        else:
            return depth_button(TextTable.objects.get(key = 'test_text_{:02}'.format(nth)).text, button_yes_or_no)

    elif button_type == 5:
        #do dosirak
        return buy_link(button.text, buttons)
    elif button_type == 6:
        #do counsel
        pass
    elif button_type == 7:
        #do faq
        if button.button_id == 7000:
            faq_items = Button.objects.annotate(val = F('button_id')/1000, mod = F('button_id')%1000).filter(val = 7).exclude(mod = 0)
            faq_buttons = [item.button_name for item in faq_items]

            return depth_button(button.text, faq_buttons)
        else:
            return depth_button(button.text, buttons)
    else:
        return not_yet()

    return depth_button(button.text, buttons)

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