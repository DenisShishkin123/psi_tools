from django import forms

from .models import ABCModel

class ABCModelForm(forms.ModelForm):
    class Meta:
        model = ABCModel
        fields = '__all__'
        # fields = ['activating', 'beliefs', 'consequences', 'emotions']
