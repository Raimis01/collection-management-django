from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Materials
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import MaterialsForm

def material_view(request):
    if request.method == 'POST':

        if request.POST['action'] == 'delete':
            selected_material_id = request.POST.get('selected_material_id')
            material_to_delete = Materials.objects.get(id=selected_material_id)
            material_to_delete.delete()

        elif request.POST['action'] == 'save':
            material_ids = request.POST.getlist('material_ids')
            for material_id in material_ids:
                # print(material_id)
                material = Materials.objects.filter(id=material_id).first()
                if material:
                    new_material = request.POST.get('material_' + material_id, material.Material)
                    material.Material = new_material
                    material.save()

        new_material = request.POST.get('new_material')
        if new_material:
            if not Materials.objects.filter(Material=new_material).exists():
                Materials.objects.create(Material=new_material)

        return redirect('material_view')

    materials = Materials.objects.all()#.order_by('-StatId')
    return render(request, 'material_view.html', {'materials': materials})