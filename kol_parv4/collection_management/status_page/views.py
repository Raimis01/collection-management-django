from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Statuses
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import StatusesForm

def status_view(request):
    if request.method == 'POST':

        if request.POST['action'] == 'delete':
            selected_status_id = request.POST.get('selected_status_id')
            status_to_delete = Statuses.objects.get(id=selected_status_id)
            status_to_delete.delete()

        elif request.POST['action'] == 'save':
            status_ids = request.POST.getlist('status_ids')
            for status_id in status_ids:
                # print(status_id)
                status = Statuses.objects.filter(id=status_id).first()
                if status:
                    new_status = request.POST.get('status_' + status_id, status.Status)
                    status.Status = new_status
                    status.save()

        new_status = request.POST.get('new_status')
        if new_status:
            if not Statuses.objects.filter(Status=new_status).exists():
                Statuses.objects.create(Status=new_status)

        return redirect('status_view')

    statuses = Statuses.objects.all()#.order_by('-StatId')
    return render(request, 'status_view.html', {'statuses': statuses})