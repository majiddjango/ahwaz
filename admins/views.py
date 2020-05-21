from django.shortcuts import render,redirect,get_object_or_404
from django.apps import apps
from core.models import Product
from comments.models import Comment
from accounts.models import MyUser
from home.models import Problem
from orders.models import Order
from datetime import timedelta,datetime
from django.utils import timezone
from django.db.models import Sum,Count
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from .forms import AdminProductForm, AdminCommentForm,AdminUserForm
from django.contrib.auth import get_user_model
@login_required
def home(request):
    if request.user.is_superuser:
        models = [
            Problem,
            Product,
            MyUser,
            Comment,
            Order
        ]
        context = {}
        context['apps'] = {}
        orders = Order.objects.filter(paid=True).aggregate(Sum('total'),Count('id'))
        now = timezone.now()
        last_week_products = Product.objects.filter(
            created_date__gte = now - timedelta(days=7)
        )
        last_day_products = Product.objects.filter(
            created_date__gte = now - timedelta(days=1)
        )
        context['title'] = 'داشبورد مدیریت'
        context['orders'] = orders
        context['last_week_products'] = last_week_products
        context['last_day_products'] = last_day_products

        for model in models:
            names = [x.name for x in model._meta.fields]
            if 'is_seen' in names:
                context['apps'][model._meta.verbose_name_plural] = model.objects.filter(is_seen=False)
            elif 'is_public' in names:
                context['apps'][model._meta.verbose_name_plural] = model.objects.filter(is_public=False)
                # print(model.objects.filter(is_public=False)._meta.verbose_name_plural)
        return render(request,'admins/home.html',context)
    else:
        return redirect('home')
    
        

    # for app in djapp.get_app_configs():
    #     print(app.verbose_name, ":")
    #     for model in app.get_models():
    #         print("\t", model.__name__,[x.name for x in model._meta.fields])



@login_required
def edit_product_admin(request,id):
    product = get_object_or_404(Product,id=id)
    if not product.is_seen:
        product.is_seen = True
        product.save()
    context ={
        'title': 'بررسی محصول'
    }
    if request.user.is_superuser:
        if request.POST:
            form = AdminProductForm(request.POST,instance=product,files=request.FILES)
            if form.is_valid():
                form.save(commit=True)
                messages.success(
                    request,
                    'تغییرات با موفقیت اعمال شد.'
                )
                return redirect('admin_home')
            else:
                context['form'] = form
                return render(request,'admins/edit.html',context)
        else:
            form = AdminProductForm(instance=product)
            context['form'] = form
            return render(request,'admins/edit.html',context)
    else:
        return redirect('home')


@login_required
def edit_comment_admin(request,id):
    com = get_object_or_404(Comment,id=id)
    if not com.is_seen:
        com.is_seen = True
        com.save()
    context ={
        'title': 'بررسی نظر',
        'com':com,
    }
    if request.user.is_superuser:
        if request.POST:
            form = AdminCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.object_id = com.object_id
                comment.content_type = com.content_type
                comment.name = request.user.username
                comment.owner = request.user
                if com.is_root_node():
                    comment.parent = com
                else:
                    comment.parent = com.get_root()

                com.is_active = comment.is_active
                com.is_deleted = comment.is_deleted
                if comment.is_deleted or comment.comment == '':
                    pass
                else:
                    comment.is_seen = True
                    form.save(commit=True)
                com.save()
                
                messages.success(
                    request,
                    'تغییرات با موفقیت اعمال شد.'
                )
                return redirect('admin_home')
            else:
                context['form'] = form
                return render(request,'admins/edit_comment.html',context)
        else:
            form = AdminCommentForm()
            context['form'] = form
            return render(request,'admins/edit_comment.html',context)
    else:
        return redirect('home')


@login_required
def edit_user_admin(request,id):
    USER = get_user_model()
    user = get_object_or_404(USER,id=id)
    if not user.is_seen:
        user.is_seen = True
        user.save()
    context ={
        'title': 'بررسی کاربر',
        'user':user,
    }
    if request.user.is_superuser:
        if request.POST:
            form = AdminUserForm(request.POST,instance=user)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'تغییرات با موفقیت اعمال شد.'
                )
                return redirect('admin_home')
            else:
                context['form'] = form
                return render(request,'admins/edit.html',context)
        else:
            form = AdminUserForm(instance=user)
            context['form'] = form
            return render(request,'admins/edit.html',context)
    else:
        return redirect('home')
