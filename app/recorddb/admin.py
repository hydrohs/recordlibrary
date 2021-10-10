from django.contrib import admin

from .models import Record, Artist

admin.site.register(Record)
admin.site.register(Artist)