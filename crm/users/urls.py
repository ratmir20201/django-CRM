from django.urls import path

from users.views import MainTitleView

app_name = "users"

urlpatterns = [path("", MainTitleView.as_view(), name="index")]
