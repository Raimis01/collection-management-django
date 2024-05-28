from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .forms import AlbumsForm, DeleteAlbumForm
from django.contrib.auth.decorators import login_required
from .models import Albums
from owner_page.models import Users
from django.db import transaction

@login_required
def album_view(request):
    if request.method == 'POST':

        if request.POST['action'] == 'delete':
            selected_album_id = request.POST.get('selected_album_id')
            album_to_delete = Albums.objects.get(AlbLocId=selected_album_id)
            album_to_delete.delete()

        elif request.POST['action'] == 'save':
            album_ids = request.POST.getlist('album_ids')
            for album_id in album_ids:
                #print(album_id)
                album = Albums.objects.filter(AlbLocId=album_id).first()
                if album:
                    new_name = request.POST.get('name_' + album_id, album.Name)
                    new_page = request.POST.get('page_' + album_id, album.Page)
                    new_page_row = request.POST.get('pageRow_' + album_id, album.PageRow)
                    new_page_col = request.POST.get('pageCol_' + album_id, album.PageCol)
                    if request.user.is_superuser:
                        username = request.POST.get('ownId_' + album_id)
                        try:
                            user = Users.objects.get(username=username)
                            album.OwnId = user
                        except Users.DoesNotExist:
                            pass

                    album.Name = new_name
                    album.Page = int(new_page)
                    album.PageRow = int(new_page_row)
                    album.PageCol = int(new_page_col)
                    album.save()

        return redirect('album_view')
    
    albums = Albums.objects.all() if request.user.is_superuser else Albums.objects.filter(OwnId=request.user.username)
    users = Users.objects.all()  
    return render(request, 'album_view.html', {'albums': albums, 'users': users})

@login_required
def create_album(request):
    if request.method == 'POST':
        form = AlbumsForm(request.POST, user=request.user)

        if form.is_valid():
            name = form.cleaned_data['Name']
            page_count = form.cleaned_data['Page']
            row_count = form.cleaned_data['PageRow']
            col_count = form.cleaned_data['PageCol']
            owner = request.user if not request.user.is_superuser else form.cleaned_data['OwnId']

            try:
                with transaction.atomic():
                    for page in range(1, page_count + 1):
                        for row in range(1, row_count + 1):
                            for col in range(1, col_count + 1):
                                alb_loc_id = f"{owner.username}-{name}-{page}-{row}-{col}"
                                album = Albums(AlbLocId=alb_loc_id, Name=name, Page=page, PageRow=row, PageCol=col, OwnId=owner)
                                album.save()
                return redirect('album_view')
            except Exception as e:
                pass
    else:
        form = AlbumsForm(user=request.user)

    return render(request, 'album_create.html', {'form': form})


@login_required
def delete_album(request):
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, user=request.user)
        if form.is_valid():
            album_name = form.cleaned_data['album_name']
            user = form.cleaned_data['user'] if request.user.is_superuser else request.user

            with transaction.atomic():
                albums_to_delete = Albums.objects.filter(Name=album_name, OwnId=user)
                for album in albums_to_delete:
                    # Collectables.objects.filter(AlbLocId=album.AlbLocId, OwnId=album.OwnId).update(AlbLocId="")
                    album.delete()

            return redirect('album_view') 
    else:
        form = DeleteAlbumForm(user=request.user)

    return render(request, 'album_delete.html', {'form': form})