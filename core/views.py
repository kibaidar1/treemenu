from django.shortcuts import render, get_object_or_404

from .models import MenuModel


def init(request):
    return render(request, 'home.html')
