from django.urls import path

from mopinion.views import about, contact, home

# domain/mopinion
urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('about', about),
]
