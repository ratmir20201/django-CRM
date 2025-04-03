from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Неверное имя пользователя или пароль.",
        "inactive": "Этот аккаунт неактивен.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите имя пользователя"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )
        self.fields["username"].label = ""
        self.fields["password"].label = ""
