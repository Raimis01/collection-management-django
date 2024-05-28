from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Conditions
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ConditionsForm

def condition_view(request):
    if request.method == 'POST':

        if request.POST['action'] == 'delete':
            selected_condition_id = request.POST.get('selected_condition_id')
            condition_to_delete = Conditions.objects.get(id=selected_condition_id)
            condition_to_delete.delete()

        elif request.POST['action'] == 'save':
            condition_ids = request.POST.getlist('condition_ids')
            for condition_id in condition_ids:
                # print(condition_id)
                condition = Conditions.objects.filter(id=condition_id).first()
                if condition:
                    new_condition = request.POST.get('condition_' + condition_id, condition.Condition)
                    condition.Condition = new_condition
                    condition.save()

        new_condition = request.POST.get('new_condition')
        if new_condition:
            if not Conditions.objects.filter(Condition=new_condition).exists():
                Conditions.objects.create(Condition=new_condition)

        return redirect('condition_view')

    conditions = Conditions.objects.all()#.order_by('-StatId')
    return render(request, 'condition_view.html', {'conditions': conditions})