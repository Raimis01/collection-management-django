from django.urls import path
from . import views

urlpatterns = [
    path('collection/allcollectables/', views.allcollectables_view, name='allcollectables_view'),
    path('collection/mycollectables/', views.mycollectables_view, name='mycollectables_view'),
    path('collection/collectable_insert/', views.collectable_insert, name='collectable_insert')
]