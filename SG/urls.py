from django.urls import path
from . import views

urlpatterns = [
    path('add', views.new_member, name='add_member')
]