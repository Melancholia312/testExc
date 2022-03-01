from django.db import models


class SomeObj(models.Model):

    date = models.DateField()
    name = models.CharField(max_length=150)
    qty = models.PositiveIntegerField(default=0)
    distance = models.PositiveIntegerField(default=0)
