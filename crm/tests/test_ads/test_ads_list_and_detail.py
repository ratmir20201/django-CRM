from http import HTTPStatus

from django.urls import reverse

from ads.models import Ads
from tests.factories.test_data_factory import TestDataFactory


class AdsListViewTestCase(TestDataFactory):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("ads:ads_list")

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_ads_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        ads = Ads.objects.all()
        ads_ = response.context["ads"]
        for a, a_ in zip(ads, ads_):
            self.assertEqual(a.pk, a_.pk)

        self.assertTemplateUsed(response, "ads/ads-list.html")


class AdDetailViewTestCase(TestDataFactory):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("ads:ads_detail", kwargs={"pk": cls.test_ad.pk})

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_ad_detail(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "ads/ads-detail.html")

        self.assertContains(response, self.test_ad.name)
        self.assertContains(response, self.test_ad.product.name)
        self.assertContains(response, self.test_ad.channel)
        self.assertContains(response, self.test_ad.budget)
