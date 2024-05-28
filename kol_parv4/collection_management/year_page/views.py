from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Years
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import YearsForm

def year_view(request):
    if request.method == 'POST':
        if request.POST['action'] == 'delete':
            selected_year_id = request.POST['selected_year_id']
            Years.objects.filter(YearId=selected_year_id).delete()

        elif request.POST['action'] == 'save':
            original_year_ids = request.POST.getlist('original_year_ids')
            for YearId in original_year_ids:
                # print(YearId)
                new_year_id = request.POST.get('updated_year_ids_' + YearId, '')
                if YearId != new_year_id and new_year_id.isdigit() and len(new_year_id) == 4:
                    if not Years.objects.filter(YearId=new_year_id).exists():
                        Years.objects.filter(YearId=YearId).update(YearId=new_year_id)

        new_year_id = request.POST.get('new_year')
        if new_year_id and new_year_id.isdigit() and len(new_year_id) == 4:
            if not Years.objects.filter(YearId=new_year_id).exists():
                Years.objects.create(YearId=new_year_id)

        return redirect('year_view')

    years = Years.objects.all()#.order_by('-YearId')
    return render(request, 'year_view.html', {'years': years})