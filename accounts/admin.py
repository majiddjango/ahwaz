from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import MyUser,Profile
from core.widgets import MapWidget
from django import forms

class CustomUserAdmin(UserAdmin):
    model = MyUser
    list_display = ('id','username','email', 'is_staff', 'is_active','is_store')
    list_filter = ('id','username','email', 'is_active','is_store')
    fieldsets = (
        (None, {'fields': ('username','email', 'password','first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_store','groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1','first_name','last_name', 'password2', 'is_staff', 'is_active','is_store')}
        ),
    )
    search_fields = ('email','username')
    ordering = ('email','username')


admin.site.register(MyUser, CustomUserAdmin)


class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'location': MapWidget
        }


class ProfileAdminForm1(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]
        widgets = {
            'location': MapWidget
        }


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ['id','user','name','last_name','phone','location']
    list_display_links = ['id','user','name']
    search_fields = ['name','user','last_name']


admin.site.register(Profile,ProfileAdmin)