from django import forms
from core.models import Product,Category
from mptt.fields import TreeNodeChoiceField
class ProductForm(forms.ModelForm):
    category = TreeNodeChoiceField(queryset=Category.objects.all())
    
    class Meta:
        model = Product
        exclude = [
            'is_seen',
            'is_deleted',
            'is_active',
            'store',
            'slug'
        ]
