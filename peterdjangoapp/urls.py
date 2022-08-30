from django.urls import path
from . import views

app_name = 'peterdjangoapp'

urlpatterns = [
    path('', views.index, name='index')
]