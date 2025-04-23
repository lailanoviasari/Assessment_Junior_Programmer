from django import forms
from .models import Mobil, Service

class MobilForm(forms.ModelForm):
    class Meta:
        model = Mobil
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'