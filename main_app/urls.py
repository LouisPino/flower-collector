from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flowers/', views.flowers_index, name='index'),
    path('flowers/<int:f_id>', views.flowers_detail, name='detail'),
    path('flowers/create', views.FlowerCreate.as_view(), name='flower_create'),
    path('flowers/<int:pk>/update', views.FlowerUpdate.as_view(), name='flower_update'),
    path('flowers/<int:pk>/delete', views.FlowerDelete.as_view(), name='flower_delete'),
    path('flowers/<int:f_id>/add_water/', views.add_watering, name='add_watering'),
    path('locations/', views.LocationIndex.as_view(), name='location_index'),
    path('locations/create', views.LocationCreate.as_view(), name='location_create'),
    path('locations/<int:l_id>', views.location_detail, name='location_detail'),
]
