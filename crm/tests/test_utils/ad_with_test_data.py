from ads.models import Ads
from tests.fixtures.test_data import test_ad_data
from tests.test_utils.product_with_test_data import ProductTestBase


class AdTestBase(ProductTestBase):
    __test__ = False

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_ad = Ads.objects.create(
            name=test_ad_data["name"],
            product=test_ad_data["product"],
            channel=test_ad_data["channel"],
            budget=test_ad_data["budget"],
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.test_ad.delete()
