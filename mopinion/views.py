from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('HOME 1')


def contact(request):
    return HttpResponse('contact')


def about(request):
    return HttpResponse('about')
