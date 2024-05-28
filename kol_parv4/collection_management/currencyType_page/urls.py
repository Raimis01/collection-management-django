from django.urls import path
from . import views

urlpatterns = [
    path('collection/currencytypes/', views.currencytype_view, name='currencytype_view')

]