from django.contrib import admin
from myapp.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']

class DietInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'types', 'button_label', 'date']

class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'text_date_day', 'text_date_holiday']

class FoodInfoAdmin(admin.ModelAdmin):
    list_display = ['restId', 'name', 'price', 'category_big', 'category_middle', 'category_small']

admin.site.register(User, UserAdmin)
admin.site.register(DietInfo, DietInfoAdmin)
admin.site.register(RestaurantInfo, RestaurantInfoAdmin)
admin.site.register(FoodInfo, FoodInfoAdmin)