from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Countries
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import CountriesForm

def country_view(request):
    if request.method == 'POST':

        if request.POST['action'] == 'delete':
            selected_country_id = request.POST.get('selected_country_id')
            country_to_delete = Countries.objects.get(CountryId=selected_country_id)
            country_to_delete.delete()

        elif request.POST['action'] == 'save':
            country_ids = request.POST.getlist('country_ids')
            for country_id in country_ids:
                
                country = Countries.objects.filter(CountryId=country_id).first()
                if country:
                    new_name = request.POST.get('countryName_' + country_id, country.Name)
                    country.Name = new_name
                    country.save()

        new_countryid = request.POST.get('new_countryid')
        new_countryname = request.POST.get('new_countryname')
        if new_countryid and new_countryname:
            if not Countries.objects.filter(CountryId=new_countryid).exists():
                Countries.objects.create(CountryId=new_countryid, Name=new_countryname)

        return redirect('country_view')

    countries = Countries.objects.all()#.order_by('-StatId')
    return render(request, 'country_view.html', {'countries': countries})