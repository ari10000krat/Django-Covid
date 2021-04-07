from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('About CODVID-19')


def about(request):
    return HttpResponse('COVID-19 Statistics')


def contact(request):
    return HttpResponse('Contact us')