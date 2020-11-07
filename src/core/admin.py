from django.contrib import admin
from .models import Static_flight_directions, Static_iata_name

# Register your models here.
admin.site.register(Static_flight_directions)
admin.site.register(Static_iata_name)