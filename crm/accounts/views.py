from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views import View

from accounts.forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    success_url = (
        ""  # TODO: Написать url (возможно нужно написать LOGIN_REDIRECT_URL в settings)
    )


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("accounts:login")
