from django.http import HttpResponse
from django.shortcuts import render

from .models import Record

def index(request):
    wishlist = Record.objects.filter(owned=False)
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'recorddb/index.html', context)