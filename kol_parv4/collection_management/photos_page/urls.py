from django.urls import path
from . import views

urlpatterns = [
    path('collection/allcollectables/photos/<str:col_id>/', views.photo_view, name='photo_view'),
    path('collection/mycollectables/photosedit/<str:col_id>/', views.photoedit_view, name='photoedit_view'),
    path('delete_photo/<str:photo_id>/', views.photo_delete, name='photo_delete')
]