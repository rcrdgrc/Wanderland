from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import uuid
import boto3
from .models import Trip, Photo
from .forms import SavingsForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'wanderland100'

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
    savings_form = SavingsForm()
    return render(request, 'trips/detail.html', { 'trip': trip, 'savings_form': savings_form })
  

def home(request):
    return render(request, 'home.html')

def add_savings(request, trip_id):
  # create the ModelForm using the data in request.POST
  form = SavingsForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_savings = form.save(commit=False)
    new_savings.trip_id = trip_id
    new_savings.save()
  return redirect('detail', trip_id=trip_id)

def add_photo(request, trip_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, trip_id=trip_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', trip_id=trip_id)