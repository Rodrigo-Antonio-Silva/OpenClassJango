from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Singers


def music_list(request):
    bands = Band.objects.all()
    return render(request,
                'listings/music_list.html',
                  {'bands': bands})


def music_detail(request, id):
    music = Band.objects.get(id=id)
    return render(request,
                  'listings/music_detail.html',
                  {'music': music})


def about(request):
    return render(request, 'listings/about.html')


def singer_list(request):
    singers = Singers.objects.all()
    return render(request,
                  'listings/singer_list.html',
                  {'singers': singers})


def singer_detail(request, id):
    singer = Singers.objects.get(id=id)
    return render(request,
                  'listings/singer_detail.html',
                  {'singer': singer})


def contact(request):
    return render(request, 'listings/contact.html')


def top6Musicas_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/top6Musicas_list.html',
                  {'bands': bands})