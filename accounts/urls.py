from django.urls import path,include
from . import views
urlpatterns = [
    # path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/update',views.update_profile,name='update_profile'),
    path('my-orders/',views.my_orders,name='my_orders'),
    # path('change-passowrd',views.change_password,name='change_password'),
] 
