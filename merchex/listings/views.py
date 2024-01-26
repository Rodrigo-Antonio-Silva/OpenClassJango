from django.shortcuts import render, redirect
from django.http import HttpResponse
from listings.models import Band, Singers
from listings.forms import ContactUsForm, MusicForm, SingerForm
from django.core.mail import send_mail


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
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anymous"} via Merchex Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent/')
    else:
        form = ContactUsForm
    form = ContactUsForm()

    return render(request,
                  'listings/contact.html',
                  {'form': form})


def top6Musicas_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/top6Musicas_list.html',
                  {'bands': bands})


def emailsent(request):
    return render(request, 'listings/send_email.html')


def music_create(request):
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            music = form.save()
            return redirect('music-detail', music.id)

    else:
        form = MusicForm()

    return render(request,
                  'listings/music_create.html',
                  {'form': form})


def singer_create(request):
    if request.method == 'POST':
        form2 = SingerForm(request.POST)
        if form2.is_valid():
            singer = form2.save()
            return redirect('singer-detail', singer.id)
    else:
        form2 = SingerForm()

    return render(request,
                  'listings/singer_create.html',
                  {'form2': form2})


def music_change(request, id):
    music = Band.objects.get(id= id)
    if request.method == 'POST':
        form = MusicForm(instance=music)
        if form.is_valid():
            form.save()
            return redirect('music-detail', music.id)
    else:
        form = MusicForm(instance=music)

    return render(request,
                  'listings/music_change.html',
                  {'form': form})


def singer_change(request, id):
    singer = Singers.objects.get(id= id)
    if request.method == 'POST':
        form2 = SingerForm(instance=singer)
        if form2.is_valid():
            form2.save()
            return redirect('singer-detail', singer.id)
    else:
        form2 = SingerForm(instance=singer)

    return render(request,
                  'listings/singer_change.html',
                  {'form2': form2})

