from django.db import models
from .RestaurantInfo import RestaurantInfo

class FoodInfo(models.Model):
    CATEGORY_BIG = (
        ('양식', '양식'),
        ('한식', '한식'),
        ('일식', '일식'),
        ('중식', '중식'),
        ('동남아', '동남아'),
        ('분식', '분식'),
    )

    CATEGORY_MIDDLE = (
        ('국/탕', '국/탕'),
        ('그라탕', '그라탕'),
        ('김밥', '김밥'),
        ('랩', '랩'),
        ('면', '면'),
        ('밥', '밥'),
        ('버거', '버거'),
        ('분식', '분식'),
        ('브리또', '브리또'),
        ('빵', '빵'),
        ('샌드위치', '샌드위치'),
        ('샐러드', '샐러드'),
        ('샐러드버거세트', '샐러드버거세트'),
        ('세트', '세트'),
        ('스파게티', '스파게티'),
        ('스프', '스프'),
        ('요리', '요리'),
        ('웜볼', '웜볼'),
        ('정식', '정식'),
        ('찜', '찜'),
        ('치킨', '치킨'),
        ('탕수육', '탕수육'),
        ('피자', '피자'),
        ('기타', '기타'),
    )

    CATEGORY_SMALL = (
        ('NONE', 'NONE'),
        ('토마토', '토마토'),
        ('크림', '크림'),
        ('로제', '로제'),
        ('오일', '오일'),
        ('기타', '기타'),
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

