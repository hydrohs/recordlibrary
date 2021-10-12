from django.urls import path

from . import views

app_name = 'recorddb'
urlpatterns = [
    path('', views.index, name = "index"),
    path('discography/<str:artist_name>', views.discog, name='discog'),
    path('list', views.list_all, name='list'),
]