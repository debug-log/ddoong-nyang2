# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .decorators import bot
import json

buttons = ['오늘 식단좀 추천 해주라!',
             '건강한 다이어트 정보가 필요해..!',
             '식습관 건강 테스트를 해보고 싶어',
             '나 병원에 가보려고해!!']

button_test = ['거식증 자가진단', '폭식증 자가진단']

food_list = ["""오늘 점심은 "의료원 종합관"에서 먹는 게 좋다냥~
나만 믿고 마음껏 먹으라냥!!

(뚝)참치김치찌개
분홍소세지전*케찹
팽이버섯야채복음
해초무침
쌀밥
별미김치"""]

poksik_list = """
    - 항상 본인의 몸무게에 대한 스트레스가 있는 편이다
    - 간식이나 식사를 하고나면 자책감 또는 불쾌감이 든다
    - 배가 부르더라도 끝까지 먹어 치우고 만다
    - 다이어트와 폭식을 반복했던 적이 있다
    - 혼자 먹는 편이 훨씬 편하다
    - 다이어트전보다 오히려 체중이 늘어버렸다
    - 남들보다 많이 먹는 편이고 뭘먹을까?도 자주 생각하는 편이다

    위 항목 중 4개 이상 해당하면 폭식증을 의심해봐야 한다냥"""

geosik_list = """
    - 주변사람들은 자신을 너무 말랐다고 하지만 나는 오히려 너무 몸무게가 많이 나간다고 생각하며, 때로는 내 몸을 증오한다
    - 식사를 최대한 적게 하려고 노력한다
    - 식사 후 일부러 구토를 하거나 설사약이나 이뇨제를 다이어트에 사용한다
    - 지속적으로 굶어 이미 건강상 손상이 나타났다
    - 음식의 조각을 헤아리거나 잘게 썰어서 먹는다
    - 음식물의 성분과 칼로리에 지나치게 집착한다

    위 항목 중 3개 이상 해당하면 거식증을 의심해봐야 한다냥"""


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