from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as authlogin,logout as authlogout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .models import Profile
from .admin import ProfileAdminForm1 as  ProfileAdminForm
from orders.models import Item, Cart

@login_required
def logout(request):

    authlogout(request)
    return redirect('home')

@login_required
def profile(request):
    user = request.user
    profile = user.profile
    context = {
        'profile':profile,
    }
    context['title'] = 'پروفایل'
    return render(request,'account/profile/profile.html',context)

@login_required
def my_orders(request):
    user = request.user
    carts = Cart.objects.filter(paid=True,closed=True,user=user)
    context = {
        'carts':carts,
        'title':'سفارشات من'
    }
    return render(request,'account/profile/my_orders.html',context)

@login_required
def update_profile(request):
    user = request.user
    profile = user.profile
    context = {}
    context['title'] = 'تغییر مشخصات کاربری'
    context['profile'] = profile
    if request.POST:
        form = ProfileAdminForm(request.POST,instance=profile,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'تغییرات با موفقیت اعمال شد.')
            return redirect('profile')
        else:
            context['form'] = form
            messages.error(request,'لطفا مجددا تلاش نمایید.')
            return render(request,'account/profile/edit.html',context)
    else:
        context['form'] = ProfileAdminForm(instance=profile)
        return render(request,'account/profile/edit.html',context)
