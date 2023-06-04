from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.models import User
from cinema.models import Ticket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


 
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
        
    context = {
        'title': 'MyCienma - Вход',
        'form': form
        }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
        
    context = {
        'title': 'MyCienma - Регистрация',
        'form': form
        }
    return render(request, 'users/registration.html', context) 

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)  
        
    context = {
        'title': 'MyCienma - Профиль',
        'form': form
        }
    return render(request, 'users/profile.html', context)    

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('cinema:index')) 

@login_required
def my_orders(request):
    tickets = Ticket.objects.filter(user=request.user)
    context = {
        'title': 'Mycinema - Главная',
        'tickets': tickets,
    }
    return render(request, 'users/my_orders.html', context)
    