from django.shortcuts import render

# Create your views here.
from dal import autocomplete

from .models import Brand


class BrandAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Brand.objects.none()

        qs = Brand.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs