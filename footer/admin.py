from django.contrib import admin

# Register your models here.
from .models import ContanctInfo,SocialNetworksLink,Footer

class ContactTabular(admin.TabularInline):
    model = ContanctInfo

class SocialNetworkTabulr(admin.TabularInline):
    model = SocialNetworksLink

class FooterAdmin(admin.ModelAdmin):
    inlines = [ContactTabular,SocialNetworkTabulr]


admin.site.register(Footer,FooterAdmin)