from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Singers


def hello(request):
    bands = Band.objects.all()
    return render(request,
                'listings/hello.html',
                  {'bands': bands})


def about(request):
    return render(request, 'listings/about.html')


def singer(request):
    singers = Singers.objects.all()
    return render(request,
                  'listings/singer.html',
                  {'singers': singers})


def contact(request):
    return render(request, 'listings/contact.html')


def ola(request):
    bands = Band.objects.all()
    return render(request, 'listings/ola.html',
                  {'bands': bands})
