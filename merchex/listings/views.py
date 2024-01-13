from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return render(request,
                'listings/hello.html',
                  {'bands': bands})


def about(request):
    return render(request, 'listings/about.html')


def list(request):
    return HttpResponse('<ul>Bandas<il>Foo fighters</il><il>Metallica</il></ul>')


def contact(request):
    return render(request, 'listings/contact.html')


def ola(request):
    bands = Band.objects.all()
    return render(request, 'listings/ola.html',
                  {'bands': bands})
