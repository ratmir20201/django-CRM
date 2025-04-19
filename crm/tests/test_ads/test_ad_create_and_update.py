from http import HTTPStatus

from django.urls import reverse

from ads.models import Ads
from tests.factories.test_data_factory import TestDataFactory


class AdCreateViewTestCase(TestDataFactory):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("ads:ads_create")

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_ad_create(self):
        data = {
            "name": "TestAdCreate",
            "product": self.test_product.id,
            "channel": "YouTube",
            "budget": "5000.00",
        }
        response = self.client.post(path=self.url, data=data)

        self.assertRedirects(response, reverse("ads:ads_list"))
        self.assertTrue(
            Ads.objects.filter(
                name=data["name"],
                product=data["product"],
                channel=data["channel"],
                budget=data["budget"],
            ).exists()
        )

    def test_get_ad_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "ads/ads-create.html")


class AdUpdateViewTestCase(TestDataFactory):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("ads:ads_update", kwargs={"pk": cls.test_ad.pk})

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_ad_update(self):
        new_data = {
            "name": "NewTestAd",
            "product": self.test_product_2.id,
            "channel": "YouTube",
            "budget": "11000.00",
        }
        response = self.client.post(self.url, data=new_data)
        self.assertRedirects(
            response,
            reverse(
                "ads:ads_detail",
                kwargs={"pk": self.test_ad.pk},
            ),
        )

        self.test_ad.refresh_from_db()
        self.assertEqual(self.test_ad.name, new_data["name"])
        self.assertEqual(self.test_ad.product.id, new_data["product"])
        self.assertEqual(self.test_ad.channel, new_data["channel"])
        self.assertEqual(str(self.test_ad.budget), new_data["budget"])

    def test_get_ad_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "ads/ads-edit.html")
