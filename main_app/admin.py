from django.contrib import admin
# Import your models here
from .models import Trip, Savings, Photo

# Register you models here
admin.site.register(Trip)
admin.site.register(Savings)
admin.site.register(Photo)