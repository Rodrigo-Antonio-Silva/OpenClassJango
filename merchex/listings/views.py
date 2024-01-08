from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def about(request):
    return HttpResponse('<h1>About us</h1> <p>We love merch!</p>')


def list(request):
    return HttpResponse('<ul>Bandas<il>Foo fighters</il><il>Metallica</il></ul>')


def contact(request):
    return HttpResponse('<p>Tel: 555-5555</h1>')
