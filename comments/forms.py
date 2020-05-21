from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = [
            'parent',
            'owner',
            'is_seen',
            'is_active',
            'is_deleted',
            'content_type',
            'object_id',
        ]

