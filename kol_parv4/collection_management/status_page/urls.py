from django.urls import path
from . import views

urlpatterns = [
    path('collection/statuses/', views.status_view, name='status_view')

]