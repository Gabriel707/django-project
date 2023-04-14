from django.urls import path

from mopinion.views import home

# domain/mopinion
urlpatterns = [
    path('', home),
]
