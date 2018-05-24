from django.db import models
from .RestaurantInfo import RestaurantInfo

class FoodInfo(models.Model):
    CATEGORY_BIG = (
        ('photo', 'photo'),
        ('text', 'text'),
    )

    CATEGORY_MIDDLE = (
        ('photo', 'photo'),
        ('text', 'text'),
    )

    CATEGORY_SMALL = (
        ('photo', 'photo'),
        ('text', 'text'),
    )

    restId = models.ForeignKey(RestaurantInfo)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    category_big = models.CharField(max_length = 20, choices=CATEGORY_BIG)
    category_middle = models.CharField(max_length = 20, choices=CATEGORY_MIDDLE)
    category_small = models.CharField(max_length = 20, choices=CATEGORY_SMALL)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

