from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='admin_home'),
    path('edit/product/<id>',views.edit_product_admin,name='edit_product_admin'),
    path('edit/comment/<id>',views.edit_comment_admin,name='edit_comment_admin'),
    path('edit/user/<id>',views.edit_user_admin,name='edit_user_admin'),
]
