from django.shortcuts import render, redirect
from django.http import HttpResponse
from listings.models import Band, Singers
from listings.forms import ContactUsForm
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
