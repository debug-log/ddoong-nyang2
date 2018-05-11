from django.contrib import admin
from myapp.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date')

class DietInfoAdmin(admin.ModelAdmin):
    list_display = ('text', 'types', 'photo_url', 'button_label', 'button_url', 'date')

admin.site.register(User, UserAdmin)
admin.site.register(DietInfo, DietInfoAdmin)