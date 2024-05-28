from django.urls import path
from . import views

urlpatterns = [
    path('collection/countries/', views.country_view, name='country_view')

]