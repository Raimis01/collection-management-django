from django.urls import path
from . import views

urlpatterns = [
    path('collection/collectables/itemprices/<str:col_id>/', views.itemprice_view, name='itemprice_view')
]