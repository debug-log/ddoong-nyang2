# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .decorators import bot
import json

buttons = ['오늘 식단좀 추천 해주라!',
             '건강한 다이어트 정보가 필요해..!',
             '식습관 건강 테스트를 해보고 싶어',
             '나 병원에 가보려고해!!']

button_yes_or_no = ['네', '아니오']

food_list = ["""오늘 점심은 "의료원 종합관"에서 먹는 게 좋다냥~
나만 믿고 마음껏 먹으라냥!!

(뚝)참치김치찌개
분홍소세지전*케찹
팽이버섯야채복음
해초무침
쌀밥
별미김치"""]

poksik_list = """
    1. 항상 본인의 몸무게에 대한 스트레스가 있는 편이다
    2. 간식이나 식사를 하고나면 자책감 또는 불쾌감이 든다
    3. 배가 부르더라도 끝까지 먹어 치우고 만다
    4. 다이어트와 폭식을 반복했던 적이 있다
    5. 혼자 먹는 편이 훨씬 편하다
    6. 다이어트전보다 오히려 체중이 늘어버렸다
    7. 남들보다 많이 먹는 편이고 뭘먹을까?도 자주 생각하는 편이다

    4개 이상 해당하면 폭식증을 의심해봐야 한다냥"""
]


diet_info = {
    'message' : {
        'text' : '이 글 읽어보고 오라냥!',
        'photo' : {
            'url' : 'https://post-phinf.pstatic.net/MjAxNzEwMjVfMTc0/MDAxNTA4ODk1NjI0NTI4.mySS4cf2tnxc4xm_-G4K_z9CjXb_aiJtyli0oz-G1XAg.-d1LGcD14o-bCIwx64z3WGiATk21u9cQxLC_yVGyoCgg.JPEG/image_1021621591508895612193.jpg?type=w1200',
            'width' : 640,
            'height' : 480
        },
        'message_button' : {
            'label' : '4가지 식사원칙',
            'url' : 'https://m.post.naver.com/viewer/postView.nhn?volumeNo=10196423&memberNo=23778630&navigationType=push'
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

def poksik_test():
    return {
        'message' : {
            'text' : poksik_list[0]
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
    user_key = request.JSON['user_key']
    types = request.JSON['type']
    content = request.JSON['content']

    if '식단' in content:
        return {
            'message' : {
                'text' : food_list[0]
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : buttons
            }
        }
    elif '다이어트' in content:
        return diet_info
    elif '병원' in content:
        return clinic_info
    elif '테스트' in content:
        return poksik_test()
    else:
        return {
            'message' : {
                'text' : '아직 준비 중입니다냥.'
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : buttons
            }
        }

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