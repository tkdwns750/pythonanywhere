from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import List
# Create your views here.
def index(request):
    all_list = List.objects.all()
    return render(request, 'foodlist/index.html', {'food_list':all_list})