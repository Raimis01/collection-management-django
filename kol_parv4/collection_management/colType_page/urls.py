from django.urls import path
from . import views

urlpatterns = [
    path('collection/coltypes/', views.coltype_view, name='coltype_view')

]