from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm

from users.models import User
from django import forms


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserCreationForm(StyleFormMixin, BaseUserCreationForm):
     class Meta:
         model = User
         fields = ('email', 'password1', 'password2')


class UserUpdateForm(StyleFormMixin, BaseUserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()