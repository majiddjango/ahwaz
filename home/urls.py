from django.urls import path,include
from . import views

urlpatterns = [
    path('about-us/',views.about_us,name='about_us'),
    path('report-to-us/',views.report_to_us,name='report_to_us')
]