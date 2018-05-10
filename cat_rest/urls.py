from django.conf.urls import url
from django.contrib import admin
from myapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/$', UserList.as_view()),
    url(r'^user/(?P<pk>[a-z0-9]+)/$', UserDetail.as_view()),
    url(r'^keyboard/', keyboard),
]
