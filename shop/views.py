from django.shortcuts import render
from django.core.paginator import Paginator
from core.models import Category,Product,Store
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.db.models import Q
from django.db.models import Max,Min
# Create your views here.

def home(request):
    context = {}
    context['title'] = 'اهواز استور:خانه'
    products = Product.actives.all()
    paginator = Paginator(products, 20) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context['products'] = products
    context['homepage'] = True
    return render(request,'shop/home.html',context)


def product(request,store,slug):
    context = {}
    product = get_object_or_404(Product,store__slug=store,slug=slug,is_active=True)
    context['product'] = product
    context['title'] = product.name
    return render(request,'shop/product_detail.html',context)
    

def store_detail(request,slug):
    context = {}
    store = get_object_or_404(Store,slug=slug)
    products = store.products.filter(is_active=True)
    
    context['products'] = products
    context['store'] = store
    context['title'] = store.name

    return render(request,'shop/store_detail.html',context)


def category_detail(request,slug):
    context = {}
    cat = get_object_or_404(Category,slug=slug)
    products = cat.products.all()
    childs = cat.get_children()
    for child in childs:
        products = products | child.products.all()
    paginator = Paginator(products, 20) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context['products'] = products
    context['cat'] = cat
    context['title'] = cat.name

    return render(request,'shop/category_detail.html',context)



def area_products(request,slug):
    context = {}
    products = Product.actives.filter(store__area__iexact=slug)
    context['products'] = products
    context['area'] = slug
    context['title'] = slug
        

    return render(request,'shop/area_products.html',context)



def search(request):
    context = {}
    context['search_page'] = True
    context['title'] = 'جستجو'
    q = request.GET.get('search','')
    if request.is_ajax():
        if len(q) >=3:
            products = Product.actives.filter(name__icontains=q)
            context['products'] = products
            return render(request,'partials/search_dropdown.html',context)

        return JsonResponse(
            {'ok':True}
        )
    else:
        ars = request.GET.getlist('area',)
        min_price = Product.actives.aggregate(Min('price'))['price__min']
        min_price1 = Product.actives.aggregate(Min('discounted_price'))['discounted_price__min']
        if min_price1 <= min_price:
            min_price = min_price1
        max_price = Product.actives.aggregate(Max('price'))['price__max']
        context['min_price'] = min_price
        context['max_price'] = max_price
        price_min = request.GET.get('price_min',min_price)
        price_max = request.GET.get('price_max',max_price)

        if price_max != max_price:
            pmax = price_max
        else:
            pmax = max_price
        
        if price_min != min_price:
            pmin = price_min
        else:
            pmin = min_price
        context['pmin'] = pmin
        context['pmax'] = pmax
        context['q'] = q
            
        if q == '':
            areas = list(set(Product.actives.values_list('store__area',flat=True)))
            context['areas'] = areas
            return render(request,'shop/search.html',context)
        if ars:
            products = Product.actives.filter(name__icontains=q)\
                .filter(Q(price__range=[pmin,pmax])|Q(discounted_price__range=[pmin,pmax]))\
                    .filter(store__area__in=ars)
        else:
            products = Product.actives.filter(name__icontains=q)\
                .filter(Q(price__range=[pmin,pmax])|Q(discounted_price__range=[pmin,pmax]))
        
        areas = list(set(products.values_list('store__area',flat=True)))
        context['products'] = products
        context['areas'] = areas
        context['ars'] = ars
        return render(request,'shop/search.html',context)


