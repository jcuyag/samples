from django.urls import path
from . import views
from . import auth


urlpatterns = [
    path('home', views.index, name='home'),
    path('index', views.index, name='index'),
    path('login', auth.login, name='login'),
    path('logout', auth.logout, name='logout'),
    path('register/', auth.register, name='register'),
    path('registered', auth.registered, name='registered'),
]