from django.db import models

class DietInfo(models.Model):
    INFOTYPE = (
        ('식단', '식단'),
        ('운동', '운동'),
    )

    text = models.TextField(null=False)
    types = models.CharField(max_length=20, choices=INFOTYPE)
    photo_url = models.CharField(max_length=256)
    button_label = models.CharField(max_length=20)
    button_url = models.CharField(max_length=256)
    day = models.IntegerField(null = False, default = 0)

    def __str__(self):
        return self.button_label

    class Meta:
        ordering = ('types',)

