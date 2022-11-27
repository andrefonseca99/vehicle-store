from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Category, Vehicle

# Create your views here.

def home(request, *args, **kwargs):
    vehicles = Vehicle.objects.filter(
        is_published=True
    ).order_by('-id')
    categories = Category.objects.filter().order_by('id')
    return render(request, 'vehicles/pages/home.html', context={
        'vehicles': vehicles,
        'categories': categories
    })

def vehicle(request, *args, **kwargs):
    vehicles = Vehicle.objects.filter(
        is_published=True
    ).order_by('-id')

    highlights_vehicles = Vehicle.objects.filter(
        is_published=True
    ).order_by('-id')[:3]

    return render(request, 'vehicles/pages/vehicles.html', context={
        'vehicles': vehicles,
        'highlights_vehicles': highlights_vehicles,
    })


class VehicleListViewBase(ListView):
    model = Vehicle
    context_object_name = 'vehicles'
    paginate_by = None
    ordering = ['-id']
    template_name = 'vehicles/pages/home.html'

class VehicleListViewHome(VehicleListViewBase):
    template_name = 'vehicles/pages/home.html'
