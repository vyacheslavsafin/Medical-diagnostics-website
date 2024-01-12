from django.contrib import admin

from medservice.models import Service, Category, Appointment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name', 'description',)

@admin.register(Service)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Appointment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'service', 'date', 'time', 'owner',)
    list_filter = ('owner',)
    search_fields = ('category', 'service',)