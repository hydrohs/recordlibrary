# Generated by Django 3.2.7 on 2021-10-09 20:36

from django.db import migrations

def link_artists(apps, schema_editor):
    Album = apps.get_model('recorddb', 'Record')
    Artist = apps.get_model('recorddb', 'Artist')
    for album in Record.objects.all():
        artist, created = Artist.objects.get_or_create(name=album.artist)
        album.artist_link = artist
        album.save()

class Migration(migrations.Migration):

    dependencies = [
        ('recorddb', '0008_auto_20211009_1735'),
    ]

    operations = [
    ]