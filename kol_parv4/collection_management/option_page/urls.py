from django.urls import path
from . import views
from year_page.views import year_view
from owner_page.views import user_view
from status_page.views import status_view
from material_page.views import material_view
from currencyValue_page.views import currencyvalue_view
from currencyType_page.views import currencytype_view
from condition_page.views import condition_view
from colType_page.views import coltype_view
from album_page.views import album_view
from country_page.views import country_view
from collectables_page.views import mycollectables_view, allcollectables_view
from ownerCol_page.views import ownercol_view

urlpatterns = [
    path('collection/main/', views.option_view, name='mainmenu'),
    path('collection/years/', year_view, name='year_view'),
    path('collection/users/', user_view, name='user_view'),
    path('collection/statuses/', status_view, name='status_view'),
    path('collection/materials/', material_view, name='material_view'),
    path('collection/currencyvalues/', currencyvalue_view, name='currencyvalue'),
    path('collection/currencytypes/', currencytype_view, name='currencytype_view'),
    path('collection/conditions/', condition_view, name='condition_view'),
    path('collection/coltypes/', coltype_view, name='coltype_view'),
    path('collection/albums/', album_view, name='album_view'),
    path('collection/countries/', country_view, name='country_view'),
    path('collection/mycollectables/', mycollectables_view, name='mycollectables_view'),
    path('collection/allcollectables/', allcollectables_view, name='allcollectables_view'),
    path('collection/ownercollections/', ownercol_view, name='ownercol_view')
    
]