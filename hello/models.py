from django.db import models

# Create your models here.
class city(models.Model):
   city_id = models.IntegerField()
   city = models.CharField(max_length=32)