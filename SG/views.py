from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

# Create your views here.
def new_member(request):
    '''
    New member
    '''

    if request.method == 'POST':
        form = NameForm(request.POST)

    #     if form.is_valid():
    #         print(form.cleaned_data)

    if form.is_bound():
        _form = {'form' : form}
    else:
        _form = form

    return render(request, 'index.html', _form)