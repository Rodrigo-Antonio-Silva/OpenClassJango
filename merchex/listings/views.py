from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
    <html>
        <head>
            <title>Hello Django</title>
        </head>
        <body>
            <h1>Hello Django!</h1>
            <p>My Favorite bands are:</p>
            <table border="1">
                <tr>
                    <th>Banda</th>
                    <th>Musicas</th>
                </tr>
                <tr>   
                    <th>{bands[0].name}</th>
                    <th>{bands[6].name}</th>
                </tr>
                <tr>   
                    <th>{bands[1].name}</th>
                    <th>{bands[7].name}</th>
                </tr>
                <tr>   
                    <th>{bands[2].name}</th>
                    <th>{bands[8].name}</th>
                </tr>
                <tr>   
                    <th>{bands[3].name}</th>
                    <th>{bands[9].name}</th>
                </tr>
                <tr>   
                    <th>{bands[4].name}</th>
                    <th>{bands[10].name}</th>
                </tr>
                <tr>   
                    <th>{bands[5].name}</th>
                    <th>{bands[11].name}</th>
                </tr>
            </table>
        </body>    
    </html>""")


def about(request):
    return HttpResponse('<h1>About us</h1> <p>We love merch!</p>')


def list(request):
    return HttpResponse('<ul>Bandas<il>Foo fighters</il><il>Metallica</il></ul>')


def contact(request):
    return HttpResponse('<p>Tel: 555-5555</h1>')
