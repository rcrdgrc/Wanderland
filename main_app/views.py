from django.shortcuts import render
from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse('<h1>Landing Page</h1>')

def about(request):
    return HttpResponse('<h1>This is the about page</h1>')