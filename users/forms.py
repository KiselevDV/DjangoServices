from django import forms
from django.forms import ValidationError

from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    """Форма для входа"""

    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data['username']
        user_to_login = CustomUser.objects.filter(username=username)
        if user_to_login.exists():
            if user_to_login.first().is_blocked:
                raise ValidationError(
                    'Данная учётная запись заблокирована')
            else:
                return self.cleaned_data
