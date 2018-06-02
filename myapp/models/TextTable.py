from django.db import models

class TextTable(models.Model):
    
    key = models.CharField(max_length=20, primary_key=True)
    text = models.TextField(null=True)
    
    def __str__(self):
        return self.key

    class Meta:
        ordering = ('key',)

