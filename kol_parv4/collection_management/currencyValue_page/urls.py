from django.urls import path
from . import views

urlpatterns = [
    path('collection/currencyvalues/', views.currencyvalue_view, name='currencyvalue_view')

]