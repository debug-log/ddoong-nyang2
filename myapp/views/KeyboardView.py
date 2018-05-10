# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .decorators import bot
import json

@bot
def on_init(request):
    return {
        'type' : 'buttons',
        'buttons' : ['1', '2', '3']
    }

@bot
def on_message(request):
    user_key = request.JSON['user_key']
    types = request.JSON['type']
    content = request.JSON['content']
    return {
        'message' : '{}님 환영합니다.'.format(user_key)
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