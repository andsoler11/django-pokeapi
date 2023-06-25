from django.db import models


class Berrie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    growth_time = models.IntegerField()
    max_harvest = models.IntegerField()
    natural_gift_power = models.IntegerField()
    size = models.IntegerField()
    smoothness = models.IntegerField()
    soil_dryness = models.IntegerField()
    firmness = models.CharField(max_length=255)
    flavors = models.JSONField()
    natural_gift_type = models.CharField(max_length=255)
    