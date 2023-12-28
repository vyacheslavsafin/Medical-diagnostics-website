from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from medservice.models import Category, Service


# def index(request):
#     return render(request, 'medservice/index.html')

class IndexView(TemplateView):
    template_name = 'medservice/index.html'


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


class ServiceCreateView(CreateView):
    model = Service
    fields = ('name', 'description', 'category', 'price', 'duration')
    success_url = reverse_lazy('medservice:all_services')


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ('name', 'description', 'category', 'price', 'duration')
    success_url = reverse_lazy('medservice:all_services')
