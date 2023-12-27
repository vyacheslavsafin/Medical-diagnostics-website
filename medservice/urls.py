from django.urls import path

from medservice.apps import MedserviceConfig
from medservice.views import index, categories, category_services, all_services

app_name = MedserviceConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/services/', category_services, name='category_services'),
    path('services/', all_services, name='all_services'),
]
