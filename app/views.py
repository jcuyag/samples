from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


# def register(request):

#     if request.method == 'GET':
#         return render(request, 'auth/register.html')

#     elif request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']
