from django.db import models


# Create your models here.
class Static_flight_directions(models.Model):
    fly_from = models.CharField(max_length=10)
    fly_to = models.CharField(max_length=10)


class Static_iata_name(models.Model):
    iata_name = models.CharField(max_length=10)
    full_name = models.CharField(max_length=150)