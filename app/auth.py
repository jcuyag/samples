from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

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
    return render(request, 'auth/register.html', {'form': RegisterForm()}) 

@login_required
def registered(request):


    if request.method == 'POST':
        _form = RegisterForm(request.POST)

        if _form.is_valid():
            print(_form.cleaned_data)

            pass1 = _form.cleaned_data.get('password')
            pass2 = _form.cleaned_data.get('confirm_password')

            if pass1 == pass2:

                # __form = dir(_form)
                return HttpResponse('success')
            else:
                raise Http404('Password did not match')

    raise Http404('ERROR')