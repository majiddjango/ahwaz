from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('product/<store>/<slug>',views.product,name='product'),
    path('store/<slug>',views.store_detail,name="store_detail"),
    path('category/<slug>',views.category_detail,name="category_detail"),
    path('area/<slug>',views.area_products,name="area_products"),
    path('search/',views.search,name='search')
]
