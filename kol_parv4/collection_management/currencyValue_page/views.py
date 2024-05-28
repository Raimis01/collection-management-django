from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import CurrencyValues
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import CurrencyValuesForm

def currencyvalue_view(request):
    if request.method == 'POST':
        if request.POST['action'] == 'delete':
            selected_currencyvalue_id = request.POST['selected_currencyvalue_id']
            CurrencyValues.objects.filter(CurrValueId=selected_currencyvalue_id).delete()

        elif request.POST['action'] == 'save':
            original_currencyvalue_ids = request.POST.getlist('original_currencyvalue_ids')
            for CurrValueId in original_currencyvalue_ids:
                # print(CurrValueId)
                new_currencyvalue_id = request.POST.get('updated_currencyvalue_ids_' + CurrValueId, '')
                if CurrValueId != new_currencyvalue_id and new_currencyvalue_id.isdigit():
                    if not CurrencyValues.objects.filter(CurrValueId=new_currencyvalue_id).exists():
                        CurrencyValues.objects.filter(CurrValueId=CurrValueId).update(CurrValueId=new_currencyvalue_id)

        new_currencyvalue_id = request.POST.get('new_currencyvalue')
        if new_currencyvalue_id and new_currencyvalue_id.isdigit() and not CurrencyValues.objects.filter(CurrValueId=new_currencyvalue_id).exists():
                CurrencyValues.objects.create(CurrValueId=new_currencyvalue_id)

        return redirect('currencyvalue_view')

    currencyvalues = CurrencyValues.objects.all()#.order_by('-CurrValueId')
    return render(request, 'currencyvalue_view.html', {'currencyvalues': currencyvalues})