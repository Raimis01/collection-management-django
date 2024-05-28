from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import CurrencyTypes
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import CurrencyTypesForm

def currencytype_view(request):
    if request.method == 'POST':

        if request.POST['action'] == 'delete':
            selected_currencytype_id = request.POST.get('selected_currencytype_id')
            currencytype_to_delete = CurrencyTypes.objects.get(id=selected_currencytype_id)
            currencytype_to_delete.delete()

        elif request.POST['action'] == 'save':
            
            currencytype_ids = request.POST.getlist('currencytype_ids')
            for currencytype_id in currencytype_ids:
                # print(currencytype_id)
                currencytype = CurrencyTypes.objects.filter(id=currencytype_id).first()
                if currencytype:
                    new_currencytype = request.POST.get('currencytype_' + currencytype_id, currencytype.CurrType)
                    currencytype.CurrType = new_currencytype
                    currencytype.save()

        new_currencytype = request.POST.get('new_currencytype')
        if new_currencytype:
            if not CurrencyTypes.objects.filter(CurrType=new_currencytype).exists():
                CurrencyTypes.objects.create(CurrType=new_currencytype)

        return redirect('currencytype_view')

    currencytypes = CurrencyTypes.objects.all()#.order_by('-StatId')
    return render(request, 'currencytype_view.html', {'currencytypes': currencytypes})