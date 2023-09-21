from django.db import models
from django.urls import reverse

from datetime import date

class Flower(models.Model):
    name = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    genus = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)
    days_between_watering = models.IntegerField("Ideal # of days between watering")
   
    def __str__(self):
        return f'{self.name}, {self.genus}, {self.id}'
      
    def get_absolute_url(self):
        return reverse("detail", kwargs={"f_id": self.id})
    
    def needs_water(self):
        if self.watering_set.last():
            return (date.today() - self.watering_set.last().date).days > self.days_between_watering
        else:
            return True
    
    
    
class Watering(models.Model):
    date= models.DateField()
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.date}'
    
    class Meta:
        ordering = ["date"]
        