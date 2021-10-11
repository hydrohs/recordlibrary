from django.http import HttpResponse
from django.shortcuts import render

from .models import Record, Artist

def index(request):
    wishlist = Record.objects.filter(owned=False).order_by('release_date')
    artists = []
    for a in Artist.objects.all():
        if wishlist.filter(artist=a.id):
            artists.append(a.name)
    artists.sort()
    context = {
        'wishlist': wishlist,
        'artists' : artists,
    }
    return render(request, 'recorddb/index.html', context)

def discog(request, artist_name):
    if Artist.objects.filter(name=artist_name).exists():
        artist_id = Artist.objects.get(name=artist_name)
        albums = Record.objects.filter(artist=artist_id).order_by('release_date')
    else:
        albums = False
    context = {
        'artist_name' : artist_name,
        'albums' : albums,

    }
    return render(request, 'recorddb/discog.html', context)
