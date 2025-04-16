from products.models import Product
from tests.fixtures.test_data import test_product_data
from tests.test_utils.auth import LoginRequiredTestsMixin


class ProductTestBase(LoginRequiredTestsMixin):
    __test__ = False

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_product = Product.objects.create(
            name=test_product_data["name"],
            description=test_product_data["description"],
            price=test_product_data["price"],
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.test_product.delete()
