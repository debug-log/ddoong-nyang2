import json
from functools import wraps
from myapp.models.User import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def bot(view_fn):
	@wraps(view_fn)
	@csrf_exempt
	def wrap(request, *args, **kwargs):
		if request.method == 'POST':
			request.JSON = json.loads(request.body.decode('utf8'))
		else:
			request.JSON = {}

		user_key = request.JSON.get('user_key')
		user_key = kwargs.get('user_key', user_key)
		if user_key:
			username = 'kakao-' + user_key
			try:
				request.user = User.objects.get(name = username)
			except User.DoesNotExist:
				request.user = User.objects.create(name = username)

		return JsonResponse(view_fn(request, *args, **kwargs) or {})
	return wrap