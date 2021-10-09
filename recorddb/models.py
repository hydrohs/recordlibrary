from django.db import models
from django.db.models.deletion import CASCADE

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Record(models.Model):
    class Condition(models.TextChoices):
        NONE = '', 'N/A'
        NEW = 'N'
        USED = 'U'
    
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)
    owned = models.BooleanField(default=False)
    condition = models.CharField(max_length=1, blank=True, choices=Condition.choices, default=Condition.NONE)

    def __str__(self):
        return self.title