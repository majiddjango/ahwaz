from django import forms

from core.models import Product,Category
from comments.models import Comment
from django.contrib.auth import get_user_model


class AdminProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('slug','brand','is_seen')

class AdminCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('owner','parent','is_seen','email','name','content_type','object_id')

    def __init__(self, *args, **kwargs):
        super(AdminCommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].required = False

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        exclude = (
            'password',
            'is_seen',
            'last_login',
            'is_superuser',
            'groups',
            'user_permissions',
            'username',
            'is_staff',
            'date_joined',
        )



