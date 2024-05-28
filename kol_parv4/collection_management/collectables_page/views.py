from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .forms import CollectablesForm
from django.contrib.auth.decorators import login_required
from .models import Collectables
from owner_page.models import Users
from django.db import transaction
from country_page.models import Countries
from year_page.models import Years
from condition_page.models import Conditions
from status_page.models import Statuses
from material_page.models import Materials
from colType_page.models import ColTypes
from currencyValue_page.models import CurrencyValues
from currencyType_page.models import CurrencyTypes
from album_page.models import Albums
from django.db.models import Max
import re
from photos_page.models import Photos
from itemPrice_page.models import ItemPrices
from decimal import Decimal
from django.db.models import Q, Subquery, OuterRef
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import render_to_string
from django.http import JsonResponse
import time
import json
from django.core.serializers.json import DjangoJSONEncoder

# # works
@login_required
def mycollectables_view(request):
    if request.method == 'POST':
        if request.POST['action'] == 'delete':
            start_time = time.time()
            selected_col_id = request.POST.get('selected_col_id')
            collectable_to_delete = Collectables.objects.get(ColId=selected_col_id)
            collectable_to_delete.delete()
            print(f"delete: {(time.time() - start_time) * 1000} milliseconds")
    

        elif request.POST['action'] == 'save':
            def get_foreign_key_object(model, pk, default):
                if pk:
                    return model.objects.filter(pk=pk).first() or default
                else:
                    return None

            col_ids = request.POST.getlist('col_ids')
            for col_id in col_ids:
                start_time = time.time()
                # print(col_id)
                collectable = Collectables.objects.filter(ColId=col_id).first()
                if collectable:
                    collectable.Name = request.POST.get('name_' + col_id, collectable.Name)
                    collectable.Description = request.POST.get('description_' + col_id, collectable.Description)
                    collectable.Country = get_foreign_key_object(Countries, request.POST.get('country_' + col_id), collectable.Country)
                    collectable.Year = get_foreign_key_object(Years, request.POST.get('year_' + col_id), collectable.Year)
                    collectable.Condition = get_foreign_key_object(Conditions, request.POST.get('condition_' + col_id), collectable.Condition)
                    collectable.Status = get_foreign_key_object(Statuses, request.POST.get('status_' + col_id), collectable.Status)
                    collectable.Material = get_foreign_key_object(Materials, request.POST.get('material_' + col_id), collectable.Material)
                    collectable.ColType = get_foreign_key_object(ColTypes, request.POST.get('colType_' + col_id), collectable.ColType)
                    collectable.CurrValue = get_foreign_key_object(CurrencyValues, request.POST.get('currValue_' + col_id), collectable.CurrValue)
                    collectable.CurrType = get_foreign_key_object(CurrencyTypes, request.POST.get('currType_' + col_id), collectable.CurrType)
                    collectable.AlbLoc = get_foreign_key_object(Albums, request.POST.get('albLoc_' + col_id), collectable.AlbLoc)
                    
                    if request.user.is_superuser:
                        collectable.Owner = get_foreign_key_object(Users, request.POST.get('owner_' + col_id), collectable.Owner)
                    
                    collectable.save()

                    print(f"save: {(time.time() - start_time) * 1000} milliseconds")
    

                    new_price_input = request.POST.get('price_' + col_id)
                    if new_price_input:
                        new_price = Decimal(new_price_input)
                        latest_price_record = ItemPrices.objects.filter(ColId=collectable).order_by('-TransDate').first()
                        if not latest_price_record or latest_price_record.Price != new_price:
                            ItemPrices.objects.create(ColId=collectable, Price=new_price)

        return redirect('mycollectables_view')

    # works
    start_time = time.time()

    collectables = Collectables.objects.all().order_by('ColId')[:20] if request.user.is_superuser else Collectables.objects.filter(Owner=request.user.username).order_by('ColId')[:20]
    # collectables = Collectables.objects.all().order_by('ColId') if request.user.is_superuser else Collectables.objects.filter(Owner=request.user.username).order_by('ColId')
    for collectable in collectables:
        latest_price = ItemPrices.objects.filter(ColId=collectable).order_by('-TransDate').first()
        collectable.latest_price = latest_price.Price if latest_price else ""

    all_albums = Albums.objects.all()  if request.user.is_superuser else Albums.objects.filter(OwnId=request.user.username)
    assigned_locations = Collectables.objects.filter(AlbLoc__isnull=False).values_list('AlbLoc__AlbLocId', flat=True).distinct()
    for collectable in collectables:
        collectable.current_location = collectable.AlbLoc
        collectable.available_albums = all_albums.exclude(AlbLocId__in=assigned_locations).union(
            Albums.objects.filter(AlbLocId=collectable.AlbLoc_id)
        )

    # paginator = Paginator(collectables, 20)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.get_page(page_number)

    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    #     html = render_to_string('_collectables_rows.html', {'collectables': page_obj})
    #     return JsonResponse({'html': html, 'has_more': page_obj.has_next()})
    
    context = {
        # 'collectables': page_obj,
        'collectables': collectables,
        'countries': Countries.objects.all(),
        'years': Years.objects.all(),
        'conditions': Conditions.objects.all(),
        'statuses': Statuses.objects.all(),
        'materials': Materials.objects.all(),
        'colTypes': ColTypes.objects.all(),
        'currValues': CurrencyValues.objects.all(),
        'currTypes': CurrencyTypes.objects.all(),
        'users': Users.objects.all()
    }

    print(f"load user: {(time.time() - start_time) * 1000} milliseconds")
    

    return render(request, 'mycollectables_view.html', context)




@login_required
def collectable_insert(request):
    if request.method == 'POST':
        form = CollectablesForm(request.POST, user=request.user)

        if form.is_valid():
            name = form.cleaned_data['Name']
            country = form.cleaned_data['Country']
            description = form.cleaned_data['Description']
            year = form.cleaned_data['Year']
            condition = form.cleaned_data['Condition']
            status = form.cleaned_data['Status']
            material = form.cleaned_data['Material']
            col_type = form.cleaned_data['ColType']
            curr_value = form.cleaned_data['CurrValue']
            curr_type = form.cleaned_data['CurrType']
            alb_loc = form.cleaned_data['AlbLoc']
            owner = request.user if not request.user.is_superuser else form.cleaned_data['Owner']
            new_price = form.cleaned_data.get('Price')

            try:
                start_time = time.time()
                

                with transaction.atomic():
                    username = request.user.username
                    
                    existing_count = Collectables.objects.filter(Owner=username).count()

                    new_number = existing_count + 1

                    col_id = f"{username}{new_number}"
                    collectable = Collectables(
                        ColId=col_id, 
                        Name=name, 
                        Country=country, 
                        Description=description,
                        Year=year,
                        Condition=condition,
                        Status=status,
                        Material=material,
                        ColType=col_type,
                        CurrValue=curr_value,
                        CurrType=curr_type,
                        AlbLoc=alb_loc,
                        Owner=owner
                    )
                    collectable.save()

                    print(f"insert: {(time.time() - start_time) * 1000} milliseconds")
    

                    if new_price is not None:
                        ItemPrices.objects.create(ColId=collectable, Price=new_price)

                return redirect('mycollectables_view')

            except Exception as e:
                pass
    else:
        form = CollectablesForm(user=request.user)

    return render(request, 'collectable_insert.html', {'form': form})


def allcollectables_view(request):
    start_time = time.time()


    collectables = Collectables.objects.filter(Owner__Show=True)
    for collectable in collectables:
        latest_price = ItemPrices.objects.filter(ColId=collectable).order_by('-TransDate').first()
        collectable.latest_price = latest_price.Price if latest_price else ""


    countries = Countries.objects.all()
    years = Years.objects.all()
    conditions = Conditions.objects.all()
    statuses = Statuses.objects.all()
    materials = Materials.objects.all()
    colTypes = ColTypes.objects.all()
    currValues = CurrencyValues.objects.all()
    currTypes = CurrencyTypes.objects.all()
    albLocs = Albums.objects.all()
    users = Users.objects.filter(Show=True)

    context = {
        'collectables': collectables,
        'countries': countries,
        'years': years,
        'conditions': conditions,
        'statuses': statuses,
        'materials': materials,
        'colTypes': colTypes,
        'currValues': currValues,
        'currTypes': currTypes,
        'albLocs': albLocs,
        'users': users
    }


    print(f"all items: {(time.time() - start_time) * 1000} milliseconds")
    
    return render(request, 'allcollectables_view.html', context)