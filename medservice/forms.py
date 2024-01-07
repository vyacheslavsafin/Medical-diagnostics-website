from django import forms

from medservice.models import Service


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ServiceForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
