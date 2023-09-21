from django.shortcuts import render
from .models import Flower

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def flowers_index(request):
   flowers = Flower.objects.all()
   return render(request, 'flowers/index.html', {
        'flowers': flowers
    })