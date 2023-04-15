
from django.shortcuts import render


def home(request):
    return render(request, 'mopinion/pages/home.html', context={
        'name': 'Gabriel Araujo',
    })
