from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index_view(request):
    value = datetime.now().date()
    context = {"today":value}
    return render(request, 'menus/index.html', context=context)


def detail(request, menu):
    return render(request, 'menus/detail.html')
