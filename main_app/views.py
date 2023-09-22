from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Flower, Location
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
   used_locations = flower.viable_locations.all().values_list('id')
   unused_locations = Location.objects.exclude(id__in=used_locations)
   
   return render(request, 'flowers/detail.html', {
        'flower': flower,
        "watering_form": WateringForm,
        "unused_locations": unused_locations
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

class LocationCreate(CreateView):
    model = Location
    fields = '__all__'
    
def location_detail(request, l_id):
   location = Location.objects.get(id=l_id)
   return render(request, 'locations/detail.html', {
        'location': location,
    })
   
class LocationIndex(ListView):
    model = Location
    
def location_add(request, f_id, l_id):
    Flower.objects.get(id=f_id).viable_locations.add(l_id)
    return redirect('detail', f_id=f_id)

def location_remove(request, f_id, l_id):
    Flower.objects.get(id=f_id).viable_locations.remove(l_id)
    return redirect('detail', f_id=f_id)
    