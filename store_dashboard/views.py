from django.shortcuts import render,redirect,get_object_or_404
from core.models import Product, Category, Store
from orders.models import Cart,Item
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm
from django.db.models import Sum,Count
# Create your views here.

@login_required
def home(request):
    user = request.user
    context = {}
    context['active_store_home'] = True
    context['title'] = 'داشبورد فروشگاهی'
    if user.is_store:
        fieldname = 'is_active'
        from django.db.models import Count
        products = Product.objects.filter(store__owner=user)
        actives = products.filter(is_active=True)
        not_actives = products.filter(is_active=False)
        items = Item.objects.filter(cart__paid=True,product__store=user.store,cart__closed=True).order_by('cart')
        sums = 0
        for item in items:
            sums += item.total_price()
        
        context['sums'] = sums
        context['items'] = items
        context['products'] = products
        context['actives'] = actives
        context['not_actives'] = not_actives

        return render(request,'store_dashboard/home.html',context)
    else:
        return redirect('home')
    
@login_required
def store_delete_product(request,id):
    user = request.user
    context = {}
    if user.is_store:
        products = get_object_or_404(Product,store__owner=user,id=id)
        products.is_deleted = True
        products.save()
        return redirect('store_home')
    else:
        return redirect('home')
@login_required
def store_update_product(request,id):
    user = request.user
    context = {}
    context['title'] = 'بروز رسانی محصول'
    if user.is_store:
        product = get_object_or_404(Product,store__owner=user,id=id)
        if request.POST:
            form = ProductForm(request.POST,instance=product,files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect('store_home')
            else:
                context['form'] = form
                return render(request,'store_dashboard/create.html',context)
        form = ProductForm(request.POST or None,instance=product)
        context['form'] = form
        return render(request,'store_dashboard/create.html',context)
    else:
        return redirect('home')

@login_required
def store_create_product(request):
    user = request.user
    context = {}
    context['title'] = 'اضافه نمودن محصول جدید'
    context['active_create'] = True
    if user.is_store:
        if request.POST:
            form = ProductForm(request.POST or None,files=request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.store = user.store
                form.save()
                return redirect('store_home')
            else:
                context['form'] = form
                return render(request,'store_dashboard/create.html',context)
        form = ProductForm(request.POST or None)
        context['form'] = form
        return render(request,'store_dashboard/create.html',context)
    else:
        return redirect('home')



@login_required
def store_orders(request):
    user = request.user
    context = {}
    context['title'] = 'بررسی سفارشات'
    context['store_orders'] = True
    if user.is_store:
        items = Item.objects.filter(cart__paid=True,product__store=user.store,cart__closed=True).order_by('cart')
        if request.POST:
            cart_id = request.POST.get('id')
            items = items.filter(cart__id=cart_id)
            for item in items:
                item.sent = True
                item.save()
            return redirect('store_orders')
        context['items'] = items
        return render(request,'store_dashboard/orders.html',context)
    else:
        return redirect('home')
