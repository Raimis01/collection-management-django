from django.urls import path
from . import views

urlpatterns = [
    path('collection/ownercollections/', views.ownercol_view, name='ownercol_view'),
]