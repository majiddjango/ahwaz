from .widgets import MapWidget
from django import forms
from .models import Product

class CustomWidgetForm(forms.Form):

    working = forms.CharField(
        # required must be false, otherwise you will get error when the toggle is off
        # at least in chrome
        required=False,
        widget=MapWidget()
    )


from dal import autocomplete
from .models import Brand

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')
        widgets = {
            'brand': autocomplete.ModelSelect2(url='brand-autocomplete')
        }