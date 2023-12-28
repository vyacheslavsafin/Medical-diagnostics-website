from django.shortcuts import render
from django.views.generic import ListView

from medservice.models import Category, Service


def index(request):
    return render(request, 'medservice/index.html')


class CategoryListView(ListView):
    model = Category


class CategoryServicesListView(ListView):
    model = Service
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class AllServicesListView(ListView):
    model = Service
