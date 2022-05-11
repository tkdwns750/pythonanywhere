from django.urls import path

from . import views

app_name = 'foodlist'
urlpatterns = [
    path('', views.index, name='index')
]