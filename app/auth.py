from django.shortcuts import render, redirect
from django.contrib import auth


def login(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    elif request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=name, password=password)

        if user:
            if user.is_active:
                auth.login(request, user)
                next = ''
                if 'next' in request.GET:
                    next = request.GET['next']

                if not next:
                    next = '/'

                return redirect('/')
            else:
                return render(request, 'auth/login.html', {'Warning': 'Your account is disabled.'})
        else:
            return render(request, 'auth/login.html', {'Warning': 'Invalid username or password'})


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
        
