from django.shortcuts import render, redirect
from .models import Photos, Collectables
from .forms import PhotosForm  # Assuming you create a form for photo upload

def photoedit_view(request, col_id):
    collectable = Collectables.objects.get(ColId=col_id)
    photos = Photos.objects.filter(ColId=collectable)

    if request.method == 'POST':
        form = PhotosForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.ColId = collectable
            new_photo.save()
            return redirect('photoedit_view', col_id=col_id)
    else:
        form = PhotosForm()

    return render(request, 'photoedit_view.html', {'collectable': collectable, 'photos': photos, 'form': form})

def photo_delete(request, photo_id):
    photo = Photos.objects.get(id=photo_id)
    col_id = photo.ColId.ColId
    photo.delete()
    return redirect('photoedit_view', col_id=col_id)

def photo_view(request, col_id):
    collectable = Collectables.objects.get(ColId=col_id)
    photos = Photos.objects.filter(ColId=collectable)

    form = PhotosForm()

    return render(request, 'photo_view.html', {'collectable': collectable, 'photos': photos, 'form': form})
