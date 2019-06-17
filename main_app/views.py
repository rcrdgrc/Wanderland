from django.shortcuts import render
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>This is the about page</h1>')