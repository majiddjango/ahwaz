from django.urls import path
from .import views
urlpatterns = [
    path('brand-autocomplete/',views.BrandAutocomplete.as_view(),name='brand-autocomplete'),
]
