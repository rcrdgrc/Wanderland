from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    budget = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.destination
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'trip_id': self.id})

class Savings(models.Model):
    date = models.DateField()
    amount = models.IntegerField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.amount} on {self.date}"
    
    class Meta:
        ordering = ['date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for trip_id: {self.trip_id} @{self.url}"
    

