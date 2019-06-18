from django.db import models
from django.urls import reverse

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    budget = models.IntegerField()

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
    

