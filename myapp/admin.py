from django.contrib import admin
from myapp.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_request', 'test_score', 'created_date']

class DietInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'types', 'button_label', 'day']

class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'text_date_day', 'text_date_holiday']

class FoodInfoAdmin(admin.ModelAdmin):
    list_display = ['restId', 'name', 'price', 'category_big', 'category_middle', 'category_small']

class ButtonAdmin(admin.ModelAdmin):
	list_display = ['button_name', 'button_id']

class TextTableAdmin(admin.ModelAdmin):
	list_display = ['key', 'text']

admin.site.register(User, UserAdmin)
admin.site.register(DietInfo, DietInfoAdmin)
admin.site.register(RestaurantInfo, RestaurantInfoAdmin)
admin.site.register(FoodInfo, FoodInfoAdmin)
admin.site.register(Button, ButtonAdmin)
admin.site.register(TextTable, TextTableAdmin)