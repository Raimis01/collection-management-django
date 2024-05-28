from django.urls import path
from . import views

urlpatterns = [
    path('collection/years/', views.year_view, name='year_view')

]