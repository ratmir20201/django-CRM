from django.urls import path

from accounts.views import CustomLoginView, CustomLogoutView

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        CustomLoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
