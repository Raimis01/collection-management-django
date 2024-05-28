from django.urls import path
from . import views

urlpatterns = [
    path('collection/materials/', views.material_view, name='material_view')

]