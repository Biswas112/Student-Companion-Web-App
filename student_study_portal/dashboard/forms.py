from django import forms
from .models import *
from django.forms import widgets
from django.contrib.auth.models import User



class Notesform(forms.ModelForm):
    class Meta:
        model=notes
        fields=['title','description']
        
class DateInput(forms.DateInput):
    input_type='date'       

class Homeworkform(forms.ModelForm):
    class Meta:
        widgets={'due':DateInput}
        model=homework
        fields=['subject','title','description','due','is_finished']

class dashboardform(forms.Form):
    text=forms.CharField(max_length=100,label='enter your search: ')
    

class todo_form(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','is_finished']
        

        

    

           