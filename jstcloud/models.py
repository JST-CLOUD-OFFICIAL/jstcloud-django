from django.db import models

# Create your models here.

class Counter(models.Model):
    count = models.IntegerField(default=0)
    gmtCreated = models.DateTimeField(auto_now_add=True)
    gmtModified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Counter({self.count})'
