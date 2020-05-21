from django.contrib import admin

from .models import About,Title,Problem
# Register your models here.


class TitleAdmin(admin.ModelAdmin):
    list_display = ['title',]

admin.site.register(Title,TitleAdmin)


class AboutAdmint(admin.ModelAdmin):
    list_display = ['id','created_date']

admin.site.register(About,AboutAdmint)


class ProblemAdmin(admin.ModelAdmin):
    list_display = ['id','owner','name','last_name','email']
    list_display_links = ['id','owner','name',]
    list_filter = ['is_seen']

admin.site.register(Problem,ProblemAdmin)