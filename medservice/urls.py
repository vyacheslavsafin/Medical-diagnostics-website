from django.urls import path

from medservice.apps import MedserviceConfig
from medservice.views import IndexView, CategoryListView, CategoryServicesListView, AllServicesListView, \
    ServiceDetailView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView, AppointmentListView, \
    AppointmentDetailView, AppointmentCreateView, AppointmentDeleteView, AppointmentUpdateView, ContactsView

app_name = MedserviceConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/services/', CategoryServicesListView.as_view(), name='category_services'),

    path('services/', AllServicesListView.as_view(), name='all_services'),
    path('services/create/', ServiceCreateView.as_view(), name='service_create'),
    path('service_view/<int:pk>', ServiceDetailView.as_view(), name='service_view'),
    path('services/<int:pk>/update/', ServiceUpdateView.as_view(), name='service_update'),
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),

    path('appointment_list/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointment_create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointment/update/<int:pk>', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointment/delete/<int:pk>', AppointmentDeleteView.as_view(), name='appointment_delete'),
]
