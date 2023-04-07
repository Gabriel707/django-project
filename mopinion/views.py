from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'mopinion/home.html', context={
        'name': 'Gabriel Araujo',
    })


def contact(request):
    return HttpResponse('contact')


def about(request):
    return HttpResponse('about')
