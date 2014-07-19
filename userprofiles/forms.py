from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationEmailForm(UserCreationForm):
    username = forms.CharField(
        max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')


class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        self.user_cache = authenticate(email=email, password=password)

        if self.user_cache is None:
            raise forms.ValidationError('User not found')
        elif not self.user_cache.is_active:
            raise forms.ValidationError('Inactive user')

        return self.cleaned_data

    def get_user(self):
        return self.user_cache
