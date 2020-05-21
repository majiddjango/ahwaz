from django.shortcuts import render,redirect,get_object_or_404
from core.models import Product
from orders.models import Cart,Item,PostPay
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm
from orders.models import Cart

# Create your views here.
@login_required
@require_http_methods(['POST',])
def add_to_cart(request,id):
    product = get_object_or_404(Product,id=id,is_active=True)
    quantity = request.POST.get('quantity')
    if int(quantity) > 0:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, closed=False)
        if product.discounted_price:
            price = product.discounted_price
        else:
            price = product.price
        try:
            item = Item.objects.get(cart=cart,product=product)
            item.quantity = item.quantity + int(quantity)
            item.price = price
            item.save()
        except Exception:
            Item.objects.create(
                cart = cart,
                product = product,
                quantity = quantity,
                name = product.name,
                price = price,
                store_name = product.store.name
            )
        messages.success(request,'به سبد کالا با موفقیت وارد شد.')
    else:
        messages.error(request, 'تعداد اشتباه وارد شده است.')
    return redirect('product',store=product.store.slug,slug=product.slug)


@login_required
def delete_item(request,id):
    item = get_object_or_404(Item,id=id,cart__user=request.user)
    item.delete()
    messages.success(request,'از سبد کالا با موفقیت حذف شد.')
    return redirect('cart')

@login_required
def cart(request):
    # items hase been loaded in context_process
    if request.POST:
        id = request.POST.get('id')
        q = int(request.POST.get('quantity',0))
        item = get_object_or_404(Item,id=id,cart__user=request.user)
        if q >=0 :
            if q == 0:
                item.delete()
                messages.success(request,'از سبد کالا با موفقیت حذف شد.')
            else:
                item.quantity = q
                item.save()
                messages.success(request,'تعداد با موفقیت تغییر کرد.')
            return redirect('cart')
        else:
            messages.error(request,'لطفا اعداد صحیح وارد کنید.')
            return redirect('cart')

    return render(request,'orders/cart.html')

@login_required
def create_order(request):
    context = {}
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            user = request.user
            cart , created = Cart.objects.get_or_create(
                user = user,
                closed = False,
            )
            ord = form.save(commit=False)
            ord.user = user
            ord.cart = cart
            ord.total = cart.total_with_pay()
            form.save(commit=True)
            cart.closed = True #baraye bastan cart 
            
            cart.paid = True # baraye pardakht

            cart.save()

            messages.success(request,'درخواست شما با موفقیت ثبت شد.')
            return redirect('create_order')
        else:
            messages.error(request,'لطفا مجددا تلاش نمایید.')
            context['form'] = form
            return render(request,'orders/create.html',context) 
    form = OrderForm()
    context['form'] = form

    return render(request,'orders/create.html',context) 
