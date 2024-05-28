from django.urls import path
from . import views

urlpatterns = [
    path('collection/users/', views.user_view, name='user_view'),
    path('collection/login/', views.user_login, name='login'),
    path('collection/register/', views.user_register, name='register'),
    path('collection/logout/', views.user_logout, name='logout')
    
]