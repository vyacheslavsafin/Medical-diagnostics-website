from django.shortcuts import render

from medservice.models import Category, Service


def index(request):
    return render(request, 'medservice/index.html')


def categories(request):
    context = {
        'object_list': Category.objects.all(),
    }
    return render(request, 'medservice/categories.html', context)


def category_services(request, pk):
    context = {
        'object_list': Service.objects.filter(category_id=pk),
    }
    return render(request, 'medservice/services.html', context)


def all_services(request):
    context = {
        'object_list': Service.objects.all(),
    }
    return render(request, 'medservice/services.html', context)
