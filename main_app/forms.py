from django.forms import ModelForm
from .models import Savings, Task

class SavingsForm(ModelForm):
  class Meta:
    model = Savings
    fields = ['date', 'amount']

class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = ['due_date', 'task']