from django import forms
from .models import *
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class FormEmployee(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class FormVehicule(ModelForm):
    class Meta:
        model = Vehicule
        fields = '__all__'