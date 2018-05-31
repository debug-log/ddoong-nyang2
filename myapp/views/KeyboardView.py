# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.models import *
from django.http import JsonResponse
from django.db.models import F

from .decorators import bot
import json, random
import datetime


t = Button.objects.annotate(mod = F('button_id')%1000).filter(mod = 0)
buttons = [item.button_name for item in t]

category_big_list = [x[0] for x in FoodInfo.CATEGORY_BIG]
category_middle_list = [x[0] for x in FoodInfo.CATEGORY_MIDDLE]
category_small_list = [x[0] for x in FoodInfo.CATEGORY_SMALL if x[0] is not 'NONE']

button_diet_info = ['오늘의 건강한 식단', '오늘의 건강한 운동 방법']

button_test = ['거식증 자가진단', '폭식증 자가진단']



poksik_list = """1. 항상 본인의 몸무게에 대한 스트레스가 있는 편이다
2. 간식이나 식사를 하고나면 자책감 또는 불쾌감이 든다
3. 배가 부르더라도 끝까지 먹어 치우고 만다
4. 다이어트와 폭식을 반복했던 적이 있다
5. 혼자 먹는 편이 훨씬 편하다
6. 다이어트전보다 오히려 체중이 늘어버렸다
7. 남들보다 많이 먹는 편이고 뭘먹을까?도 자주 생각하는 편이다

위 항목 중 4개 이상 해당하면 폭식증을 의심해봐야 한다냥"""

geosik_list = """1. 주변사람들은 자신을 너무 말랐다고 하지만 나는 오히려 너무 몸무게가 많이 나간다고 생각하며, 때로는 내 몸을 증오한다
2. 식사를 최대한 적게 하려고 노력한다
3. 식사 후 일부러 구토를 하거나 설사약이나 이뇨제를 다이어트에 사용한다
4. 지속적으로 굶어 이미 건강상 손상이 나타났다
5. 음식의 조각을 헤아리거나 잘게 썰어서 먹는다
6. 음식물의 성분과 칼로리에 지나치게 집착한다

위 항목 중 3개 이상 해당하면 거식증을 의심해봐야 한다냥"""

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


poksik_test = {
    'message' : {
        'text' : poksik_list
    },
    'keyboard' : {
        'type' : 'buttons',
        'buttons' : buttons
    }
}

geosik_test = {
    'message' : {
        'text' : geosik_list
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
    elif '테스트' in content:
        return {
            'message' : {
                'text' : '어떤 테스트를 해보고 싶냥?'
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : button_test
            }
        }
    elif '폭식증' in content:
        return poksik_test
    elif '거식증' in content:
        return geosik_test
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