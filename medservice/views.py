from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from medservice.forms import ServiceForm, AppointmentForm
from medservice.models import Category, Service, Appointment


class IndexView(TemplateView):
    template_name = 'medservice/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['objects'] = Category.objects.all()[:3]

        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class ContactsView(TemplateView):
    template_name = 'medservice/contacts.html'


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['objects'] = Category.objects.all()

        return context_data


class CategoryServicesListView(ListView):
    model = Service

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_description = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['description'] = category_description.description
        context_data['title'] = category_description.description

        return context_data


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

    def get_form(self, form_class=AppointmentForm):
        field = self.request.GET.get('from')
        if field is None:
            return form_class(**self.get_form_kwargs())
        service = Service.objects.get(pk=field)
        form_data = self.get_form_kwargs()
        form_data['initial']['category'] = service.category
        form_data['initial']['service'] = service
        return form_class(**form_data)


class AppointmentDetailView(DetailView):
    model = Appointment


class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy('medservice:appointment_list')


class AppointmentDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy('medservice:appointment_list')
