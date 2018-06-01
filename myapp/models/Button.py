from django.db import models

class Button(models.Model):
    
    button_name = models.TextField(null=False)
    button_id = models.IntegerField(primary_key=True)
    text = models.TextField(null=True)
    
    def __str__(self):
        return self.button_name

    class Meta:
        ordering = ('button_id',)

