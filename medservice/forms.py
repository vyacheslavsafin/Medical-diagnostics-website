from django import forms
from medservice.models import Service, Appointment


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ServiceForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class AppointmentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('service', 'date', 'time', 'owner',)
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'time': forms.TimeInput(
                attrs={'type': 'time', 'placeholder': 'hh-mm (DOB)', 'class': 'form-control'}
            )
        }
