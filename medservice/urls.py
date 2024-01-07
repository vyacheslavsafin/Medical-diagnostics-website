from django.urls import path

from medservice.apps import MedserviceConfig
from medservice.views import IndexView, CategoryListView, CategoryServicesListView, AllServicesListView, \
    ServiceDetailView, ServiceCreateView, ServiceUpdateView

app_name = MedserviceConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/services/', CategoryServicesListView.as_view(), name='category_services'),
    path('services/', AllServicesListView.as_view(), name='all_services'),
    path('service_view/<int:pk>', ServiceDetailView.as_view(), name='service_view'),
    path('services/create/', ServiceCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/update/', ServiceUpdateView.as_view(), name='service_update'),
    # path('services/<int:pk>/delete/', AllServicesListView.as_view(), name='all_services'),
]
