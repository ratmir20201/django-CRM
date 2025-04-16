from http import HTTPStatus

from django.urls import reverse

from products.models import Product
from tests.fixtures.test_data import test_ad_data
from tests.test_utils.ad_with_test_data import AdTestBase
from tests.test_utils.product_with_test_data import ProductTestBase


class AdCreateViewTestCase(ProductTestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("ads:ads_create")

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_ad_create(self):
        response = self.client.post(path=self.url, data=test_ad_data)

        self.assertRedirects(response, reverse("ads:ads_list"))
        self.assertTrue(
            Product.objects.filter(
                name=test_ad_data["name"],
                product=test_ad_data["product"],
                channel=test_ad_data["channel"],
                budget=test_ad_data["budget"],
            ).exists()
        )

    def test_get_ad_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "ads/ads-create.html")


class AdUpdateViewTestCase(AdTestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("ads:ads_update", kwargs={"pk": cls.test_ad.pk})

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_ad_update(self):
        new_data = {
            "name": "NewTestAd",
            "product": 1,
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
        self.assertEqual(self.test_ad.name, "NewTestAd")
        self.assertEqual(self.test_ad.product, 1)
        self.assertEqual(self.test_ad.channel, "YouTube")
        self.assertEqual(str(self.test_ad.budget), "11000.00")

    def test_get_ad_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "ads/ads-edit.html")
