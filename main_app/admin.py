from django.contrib import admin
from .models import Flower, Watering, Location
# Register your models here.
admin.site.register(Flower)
admin.site.register(Watering)
admin.site.register(Location)