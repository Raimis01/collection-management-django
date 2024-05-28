from django.urls import path
from . import views

urlpatterns = [
    path('collection/conditions/', views.condition_view, name='condition_view')

]