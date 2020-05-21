from django.shortcuts import render
from comments.forms import CommentForm
from comments.models import Comment


from django import template

register = template.Library()

@register.filter
def count_me(item):
    comments = Comment.objects.for_model(item)
    return comments.count()
@register.inclusion_tag('comments/commentForm.html')
def showform(item):
    id = item.id
    model_name = item._meta.model.__name__
    app_name = item._meta.app_label
    form = CommentForm()
    return {
        'id':id,
        'form':form,
        'model_name':model_name,
        'app_name':app_name,
        'item':item,
    }

@register.inclusion_tag('comments/list.html')
def showcomments(item):
    id = item.id
    model_name = item._meta.model.__name__
    app_name = item._meta.app_label
    comments = Comment.objects.for_model(item)

    form = CommentForm()
    return {
        'id':id,
        'form':form,
        'model_name':model_name,
        'app_name':app_name,
        'item':item,
        'comments':comments,
    }
