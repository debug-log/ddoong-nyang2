from django.conf.urls import url
from django.contrib import admin
from myapp.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/$', UserList.as_view()),
    url(r'^user/(?P<pk>[a-z0-9]+)/$', UserDetail.as_view()),
    url(r'^dietinfo/$', csrf_exempt(DietInfoList.as_view())),
    url(r'^dietinfo/(?P<pk>[a-z0-9]+)/$', csrf_exempt(DietInfoDetail.as_view())),
    url(r'^keyboard/', on_init),
    url(r'^message', on_message),
    url(r'^friend', on_added),
    url(r'^friend/(?P<user_key>[\w-]+)$', on_block),
    url(r'^chat_room/(?P<user_key>[\w-]+)$', on_leave),    
]
