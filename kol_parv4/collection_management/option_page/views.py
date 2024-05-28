from django.shortcuts import render

def option_view(request):
    
    context = {
        'year_view_url': 'collection/years/',
        'user_view_url': 'collection/users/',
        'status_view_url': 'collection/statuses/',
        'material_view_url': 'collection/materials/',
        'currencyvalue_view_url': 'collection/currencyvalues/',
        'currencytype_view_url': 'collection/currencytypes/',
        'condition_view_url': 'collection/conditions/',
        'coltype_view_url': 'collection/coltypes/',
        'album_view_url': 'collection/albums/',
        'country_view_url': 'collection/countries/',
        'mycollectables_view_url': 'collection/mycollectables/',
        'allcollectables_view_url': 'collection/allcollectables/',
        'ownercol_view_url': 'collection/ownercollections/'
    }
    return render(request, 'option_view.html', context)
