from django import forms
from .models import Order
from core.widgets import MapWidget
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ['user','paid','cart','total']
        widgets = {
            'location': MapWidget
        }
