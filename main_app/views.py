from django.shortcuts import render

flowers = [
  {'name': 'Toffee', 'colors': ['brown'], 'description': 'A light brown rose', 'genus': 'Rosa'},
  {'name': 'Knockout', 'colors': ['pink', 'red'], 'description': 'A bush filled covered with roses', 'genus': 'Rosa'}, 
  {'name': 'Moonshadow', 'colors': ['purple', 'pink'], 'description': 'A soft and subtly hued rose', 'genus': 'Rosa'}, 
  {'name': 'Endless Summer', 'colors': ['purple', 'blue'], 'description': 'A bush with pom-pom shaped flowers.', 'genus': 'Hydrangea'}, 
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def flowers_index(request):
   return render(request, 'flowers/index.html', {
        'flowers': flowers
    })