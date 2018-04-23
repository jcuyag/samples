from django.urls import path
from . import views
from . import auth


urlpatterns = [
    path('', views.index, name='index page'),
    path('login', auth.login, name='login'),
    path('logout', auth.logout, name='logout'),
    path('register', auth.register, name='register'),
]