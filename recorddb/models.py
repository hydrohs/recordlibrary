from django.db import models

class Record(models.Model):
    class Condition(models.TextChoices):
        NONE = '', 'N/A'
        NEW = 'N'
        USED = 'U'
    
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    owned = models.BooleanField(default=False)
    condition = models.CharField(max_length=1, blank=True, choices=Condition.choices, default=Condition.NONE)

    def __str__(self):
        return self.title