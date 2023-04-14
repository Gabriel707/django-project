from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'mopinion/home.html', context={
        'name': 'Gabriel Araujo',
    })


def contact(request):
    return HttpResponse('Reach me out on linkedin: https://www.linkedin.com/in/gabrieldesantana11/')


def about(request):
    return HttpResponse('about')
