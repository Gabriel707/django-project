from django.urls import path

from mopinion.views import about, contact, home

urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('about', about),
]
