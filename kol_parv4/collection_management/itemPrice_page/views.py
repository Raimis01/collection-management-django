from django.shortcuts import render, get_object_or_404
from .models import Collectables, ItemPrices

def itemprice_view(request, col_id):
    collectable = get_object_or_404(Collectables, ColId=col_id)
    itemprices = ItemPrices.objects.filter(ColId=collectable).order_by('-TransDate')

    return render(request, 'itemprice_view.html', {'collectable': collectable, 'itemprices': itemprices})
