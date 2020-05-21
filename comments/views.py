from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_http_methods
from django.apps import apps
from django.http import Http404
from .forms import CommentForm
from django.contrib import messages
from .models import Comment
# Create your views here.
@require_http_methods(["POST",])
def post_comment(request):
    id = request.POST.get('id',0)
    model_name = request.POST.get('model_name','')
    app_name = request.POST.get('app_name','')
    next_item = request.POST.get('next')
    if id == 0 or model_name == '' or app_name == '':
        return Http404

    model = apps.get_model(app_name,model_name)

    item = get_object_or_404(model,id=id,is_active=True,is_deleted=False)
    user = request.user
    form = CommentForm(request.POST)
    if form.is_valid():
        com = form.save(commit=False)
        if user.is_authenticated:
            com.owner = user
        com.content_object = item
        form.save()
        messages.success(request,'نظر شما با موفقیت ثبت شد. با تشکر')
        return redirect(next_item or 'home')
    else:
        messages.error(request,'لطفا مجددا تلاش نمایید.')
        return redirect(next_item or 'home')

@require_http_methods(["POST",])
def reply_comment(request):
    id = request.POST.get('id',0)
    model_name = request.POST.get('model_name','')
    app_name = request.POST.get('app_name','')
    cid = request.POST.get('cid',0)
    next_item = request.POST.get('next')
    if id == 0 or model_name == '' or app_name == '' or cid == 0:
        return Http404

    model = apps.get_model(app_name,model_name)

    item = get_object_or_404(model,id=id,is_active=True,is_deleted=False)
    comment = get_object_or_404(Comment,id=cid,is_active=True,is_deleted=False)
    user = request.user
    form = CommentForm(request.POST)
    if form.is_valid():
        com = form.save(commit=False)
        if user.is_authenticated:
            com.owner = user
        com.content_object = item
        com.parent = comment
        form.save()
        messages.success(request,'نظر شما با موفقیت ثبت شد. با تشکر')
        return redirect(next_item or 'home')
    else:
        messages.error(request,'لطفا مجددا تلاش نمایید.')
        return redirect(next_item or 'home')



