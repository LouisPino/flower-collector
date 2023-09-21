from django.db import models
from django.urls import reverse

class Flower(models.Model):
    name = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    genus = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)
    
    def __str__(self):
        return f'{self.name}, {self.genus}, {self.id}'
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"f_id": self.id})
    