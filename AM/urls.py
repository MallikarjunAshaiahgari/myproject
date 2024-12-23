from django.urls import path
from .views import *

app_name='AM'

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('delete/', delete, name='delete'),
    path('edit/', edit, name='edit')
]