from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Collectables, OwnersCol, ColTypes
from django.shortcuts import render
#from django.db.models import Distinct

@receiver(post_save, sender=Collectables)
def update_owners_col(sender, instance, **kwargs):
    owner = instance.Owner

    OwnersCol.objects.filter(Owner=owner).delete()

    unique_col_types = Collectables.objects.filter(Owner=owner).values('ColType').distinct()

    for col_type in unique_col_types:
        OwnersCol.objects.create(
            ColType=ColTypes.objects.get(pk=col_type['ColType']),
            Owner=owner
        )

def ownercol_view(request):
    ownerscol = OwnersCol.objects.filter(Owner__Show=True)

    return render(request, 'ownercol_view.html', {'ownerscol': ownerscol})