from django.contrib import admin

# Register your models here.
from .models import Cart,Item,PostPay,Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','store_name','quantity','price','product']
    list_display_links = ['name','store_name',]

admin.site.register(Item,ItemAdmin)

class CartAdmin(admin.ModelAdmin):
    list_filter = ['user','paid','closed']
    list_display = ['id','user','closed','paid']
    list_display_links = ['id','user']

admin.site.register(Cart,CartAdmin)

class PostPayAdmin(admin.ModelAdmin):
    list_display = ['id','post']
    list_display_links = ['id','post']

admin.site.register(PostPay,PostPayAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_filter = ['user','paid',]
    list_display = ['id','user','paid','total']
    list_display_links = ['id','user',]

admin.site.register(Order,OrderAdmin)

