from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','owner','parent','email','is_active','created_date']
    list_display_links = ['id','owner','parent']

    list_filter = ['owner','is_active','is_seen']
    search_fields =  ['owner','comment']


admin.site.register(Comment,CommentAdmin)