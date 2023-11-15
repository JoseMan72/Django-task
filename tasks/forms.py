from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['title', 'description', 'completed']
'''
class TaskForm(forms.Form):
  title = forms.CharField(max_length=50)
  description = forms.CharField(widget=forms.Textarea ,max_length=200)
  completed = forms.BooleanField(required=False)
'''