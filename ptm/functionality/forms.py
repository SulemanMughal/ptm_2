from django import forms
from .models import properties

class propertyform(forms.ModelForm):
    class Meta:
        model = properties
        exclude = ['user','date']