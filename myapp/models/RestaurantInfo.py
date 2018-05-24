from django.db import models

class RestaurantInfo(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    text_date_day = models.TextField()
    text_date_holiday = models.TextField(null = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

