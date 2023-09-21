from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Flower
from .forms import WateringForm

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
    
def flowers_detail(request, f_id):
   flower = Flower.objects.get(id=f_id)
   return render(request, 'flowers/detail.html', {
        'flower': flower,
        "watering_form": WateringForm
    })
   
class FlowerCreate(CreateView):
    model = Flower
    fields = '__all__'
   
class FlowerUpdate(UpdateView):
    model = Flower
    fields = ['genus', 'description', 'photo']
    
class FlowerDelete(DeleteView):
    model = Flower
    success_url='/flowers'
    
    
def add_watering(request, f_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.flower_id = f_id
        new_watering.save()
    return redirect('detail', f_id = f_id)