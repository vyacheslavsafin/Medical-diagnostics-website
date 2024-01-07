from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy

from medservice.forms import ServiceForm
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
    form_class = ServiceForm
    success_url = reverse_lazy('medservice:all_services')


class ServiceDetailView(DetailView):
    model = Service
    extra_context = {
        'title': 'Описание услуги'
    }


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('medservice:all_services')
