from django.db import models

# Create your models here.

class Counter(models.Model):
    class Meta:
        db_table = "counter"

    id = models.AutoField(primary_key=True)
    count = models.IntegerField(default=0)
    gmtCreated = models.DateTimeField(auto_now_add=True, db_column="gmt_created")
    gmtModified = models.DateTimeField(auto_now=True, db_column="gmt_modified")
    
    def __str__(self):
        return f'Counter({self.count})'
