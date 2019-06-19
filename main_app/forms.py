from django.forms import ModelForm
from .models import Savings

class SavingsForm(ModelForm):
  class Meta:
    model = Savings
    fields = ['date', 'amount']