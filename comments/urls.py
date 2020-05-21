from django.urls import path
from . import views

urlpatterns = [
    path('post',views.post_comment,name='post_comment'),
    path('reply',views.reply_comment,name="reply_comment"),
] 
