from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_request = models.IntegerField(null = False, default = 0)
    test_score = models.IntegerField(null = False, default = 0)
    content = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_date',)
