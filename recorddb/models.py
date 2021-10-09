from django.db import models

class Record(models.Model):
    class Condition(models.TextChoices):
        NEW = 'N'
        USED = 'U'
    
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    owned = models.BooleanField
    condition = models.CharField(max_length=1, choices=Condition.choices, default=Condition.NEW)

    def __str__(self):
        return self.title