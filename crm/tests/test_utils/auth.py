from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class LoginRequiredTestsMixin(TestCase):
    __test__ = False

    url = None

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(
            username="TestUser",
            password="TestPassword",
        )

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client.force_login(self.user)

    def assert_login_required(self):
        """Тест для редиректа на страницу логина, если пользователь не авторизован."""
        self.client.logout()
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"{reverse('accounts:login')}?next={self.url}")
