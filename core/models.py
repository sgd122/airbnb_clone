from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ TimeStampedModel Model Definition """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # DB에는 생성되지않음. 확장성.

