from django.contrib import admin
from myapp.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date')

admin.site.register(User, UserAdmin)