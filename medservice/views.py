from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from medservice.forms import ServiceForm, AppointmentForm
from medservice.models import Category, Service, Appointment


class IndexView(TemplateView):
    template_name = 'medservice/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['objects'] = Category.objects.all()

        return context_data


class ContactsView(TemplateView):
    template_name = 'medservice/contacts.html'


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


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('medservice:all_services')


class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Appointment.objects.filter(owner=self.request.user)
        else:
            return Appointment.objects.all()


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy('medservice:appointment_list')

    def get_form(self, form_class=AppointmentForm, **kwargs):
        field = self.request.GET.get('from')
        if field is None:
            return form_class(**kwargs)
        service = Service.objects.get(pk=field)
        return form_class(initial={'category': service.category, 'service': service})


class AppointmentDetailView(DetailView):
    model = Appointment
    extra_context = {
        'title': 'Запись на приём к врачу'
    }


class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy('medservice:appointment_list')


class AppointmentDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy('medservice:appointment_list')
