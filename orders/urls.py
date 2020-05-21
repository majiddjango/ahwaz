from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.cart,name='cart'),
    path('order/create',views.create_order,name='create_order'),
    path('product/<id>/',views.add_to_cart,name='add_to_cart'),
    path('delete/item/<id>',views.delete_item,name='delete_item'),
]
