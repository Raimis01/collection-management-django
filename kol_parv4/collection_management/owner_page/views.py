from django.shortcuts import render, redirect, get_object_or_404
from .models import Users
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .forms import UsersForm
from django.contrib.auth.decorators import login_required


def user_register(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainmenu')
    else:
        form = UsersForm()
    
    return render(request, 'user_register.html', {'form': form})



@login_required
def user_view(request):
    User = get_user_model()
    if request.method == 'POST':

        if request.POST['action'] == 'delete':
            selected_user_username = request.POST.get('selected_user_username')
            user_to_delete = User.objects.get(id=selected_user_username)
            user_to_delete.delete()
            return redirect('user_view' if request.user.is_superuser else 'mainmenu')

        elif request.POST['action'] == 'save':
            user_usernames = request.POST.getlist('user_usernames')
            for user_username in user_usernames:
                print(user_username)
                user = User.objects.filter(username=user_username).first()
                if user:
                    new_first_name = request.POST.get('first_name_' + user_username, user.first_name)
                    new_last_name = request.POST.get('last_name_' + user_username, user.last_name)
                    new_email = request.POST.get('email_' + user_username, user.email)
                    new_telephone = request.POST.get('telephone_' + user_username, user.Telephone)

                    user.Show = ('show_' + user_username) in request.POST
                    user.is_superuser = ('is_superuser_' + user_username) in request.POST
                    user.first_name = new_first_name
                    user.last_name = new_last_name
                    user.email = new_email
                    user.Telephone = new_telephone
                    user.save()

            return redirect('user_view')
    
    users = User.objects.all() if request.user.is_superuser else User.objects.filter(username=request.user.username)

    return render(request, 'user_view.html', {'users': users})



def user_login(request):
    if request.method == "POST":


        username = request.POST.get('username')  
        password = request.POST.get('password')

        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('mainmenu')
        
    return render(request, 'login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return redirect('mainmenu')