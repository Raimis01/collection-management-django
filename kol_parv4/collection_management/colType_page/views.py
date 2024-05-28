from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import ColTypes
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ColTypesForm

def coltype_view(request):
    if request.method == 'POST':

        if request.POST['action'] == 'delete':
            selected_coltype_id = request.POST.get('selected_coltype_id')
            coltype_to_delete = ColTypes.objects.get(id=selected_coltype_id)
            coltype_to_delete.delete()

        elif request.POST['action'] == 'save':
            coltype_ids = request.POST.getlist('coltype_ids')
            for coltype_id in coltype_ids:
                #print(coltype_id)
                coltype = ColTypes.objects.filter(id=coltype_id).first()
                if coltype:
                    new_coltype = request.POST.get('coltype_' + coltype_id, coltype.ColType)
                    coltype.ColType = new_coltype
                    coltype.save()

        new_coltype = request.POST.get('new_coltype')
        if new_coltype:
            if not ColTypes.objects.filter(ColType=new_coltype).exists():
                ColTypes.objects.create(ColType=new_coltype)

        return redirect('coltype_view')

    coltypes = ColTypes.objects.all()#.order_by('-StatId')
    return render(request, 'coltype_view.html', {'coltypes': coltypes})