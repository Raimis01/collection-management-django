from django.urls import path
from . import views

urlpatterns = [
    path('collection/albums/', views.album_view, name='album_view'),
    path('collection/album_create/', views.create_album, name='create_album'),
    path('collection/album_delete/', views.delete_album, name='delete_album')

]