from django.db import models
from django.urls import reverse

class Flower(models.Model):
    name = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    genus = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)
    days_between_watering = models.IntegerField()
   
    def __str__(self):
        return f'{self.name}, {self.genus}, {self.id}'
      
    def get_absolute_url(self):
        return reverse("detail", kwargs={"f_id": self.id})
    
    
    
class Watering(models.Model):
    date= models.DateField()
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.date}'
