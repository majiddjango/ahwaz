from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('',views.home,name='store_home'),
    path('delete/<id>',views.store_delete_product,name='store_delete_product'),
    path('update/<id>',views.store_update_product,name='store_update_product'),
    path('create/',views.store_create_product,name='store_create_product'),
    path('store_orders/',views.store_orders,name='store_orders'),

] 
