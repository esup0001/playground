from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Username', max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(
        label="Password", strip=False, widget=forms.PasswordInput(
            attrs={"autocomplete": "off", 'class': 'form-control', 'placeholder': 'Password'}),
    )


class AppLogin(LoginView):
    form_class = LoginForm
    next_page = 'home'
    template_name = 'project_management/pages/login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Username atau password salah, silakan coba lagi.')
        return super().form_invalid(form)


def app_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
