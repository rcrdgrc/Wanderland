from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trip


class TripUpdate(UpdateView):
  model = Trip
  # Let's make it impossible to rename a trip :)
  fields = ['start_date', 'end_date', 'budget']

class TripDelete(DeleteView):
  model = Trip
  success_url = '/trips/'

class TripCreate(CreateView):
  model = Trip
  fields = '__all__'
  success_url = '/trips/'

def trips_index(request):
    trips = Trip.objects.all()
    return render(request, 'trips/index.html', { 'trips': trips })

def trips_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'trips/detail.html', { 'trip': trip })

def home(request):
    return render(request, 'home.html')
