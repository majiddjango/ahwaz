from django.contrib import admin
from django import forms

# Register your models here.
from .models import Category,Store,Product,Brand
from mptt.admin import DraggableMPTTAdmin
from mptt.admin import MPTTModelAdmin
from django.utils.html import format_html
from .widgets import MapWidget
from .froms import ProductForm


class CategoryAdminDragable(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'name','slug')
    list_display_links = ('name',)
    exclude = ['slug',]
    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,  # Or whatever you want to put here
        )
    something.short_description = 'something nice'

admin.site.register(Category,CategoryAdminDragable)

class StoreAdminForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
        widgets = {
            'location': MapWidget
        }



class StoreAdmin(admin.ModelAdmin):
    form = StoreAdminForm
    list_display = ['id','name','slug','location','owner','phone','area','is_active'] 
    list_display_links = ['id','name',]
    search_fields = ['id','name','area']
    list_filter = ['is_active']
    preserve_filters = True

admin.site.register(Store,StoreAdmin)

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['id','name','category','store','price','discounted_price','is_active','created_date'] 
    list_display_links = ['id','name',]
    search_fields = ['id','name','store']
    list_filter = ['is_active','store']
    exclude = ['is_seen','slug']
    preserve_filters = True
    
admin.site.register(Product,ProductAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','slug',]
    list_display_links = ['name']
    preserve_filters = True

admin.site.register(Brand,BrandAdmin)