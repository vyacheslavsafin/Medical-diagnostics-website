from django.urls import path

from medservice.apps import MedserviceConfig
from medservice.views import index, CategoryListView, CategoryServicesListView, AllServicesListView

app_name = MedserviceConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/services/', CategoryServicesListView.as_view(), name='category_services'),
    path('services/', AllServicesListView.as_view(), name='all_services'),
]
