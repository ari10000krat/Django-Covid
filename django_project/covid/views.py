from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'covid/index.html')
    # return HttpResponse('About CODVID-19')


def about(request):
    return render(request, 'covid/about.html')


def contact(request):
    return render(request, 'covid/contact.html')
