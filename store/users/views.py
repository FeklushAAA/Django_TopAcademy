from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse

from users.models import User

def login(request):
    if request.method == 'post':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            #аутентифицируем пользователя с определенными данными.
            #алее передаем аргументы в username и пароль
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)

def register(request):
    return render(request, 'users/register.html')