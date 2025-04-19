from http import HTTPStatus

from django.urls import reverse

from ads.models import Ads
from tests.factories.test_data_factory import TestDataFactory


class AdDeleteViewTestCase(TestDataFactory):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("ads:ads_delete", kwargs={"pk": cls.test_ad.pk})

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_ad_delete(self):
        response = self.client.post(self.url)

        self.assertRedirects(response, reverse("ads:ads_list"))
        self.assertFalse(Ads.objects.filter(pk=self.test_ad.pk).exists())

    def test_get_ad_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "ads/ads-delete.html")
