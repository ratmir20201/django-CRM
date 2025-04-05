from http import HTTPStatus

from django.urls import reverse

from products.models import Product
from tests.fixtures.one_test_product import test_product_data
from tests.test_utils.auth import LoginRequiredTestsMixin
from tests.test_utils.product_with_test_data import ProductTestBase


class ProductCreateViewTestCase(LoginRequiredTestsMixin):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("products:product_create")

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_product_create(self):
        response = self.client.post(path=self.url, data=test_product_data)

        self.assertRedirects(response, reverse("products:products_list"))
        self.assertTrue(
            Product.objects.filter(
                name=test_product_data["name"],
                description=test_product_data["description"],
                price=test_product_data["price"],
            ).exists()
        )

    def test_get_product_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "products/products-create.html")


class ProductUpdateViewTestCase(ProductTestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("products:product_update", kwargs={"pk": cls.test_product.pk})

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_product_update(self):
        new_data = {
            "name": "Updated Name",
            "description": "Updated description",
            "price": "2000.00",
        }
        response = self.client.post(self.url, data=new_data)
        self.assertRedirects(
            response,
            reverse(
                "products:product_detail",
                kwargs={"pk": self.test_product.pk},
            ),
        )

        self.test_product.refresh_from_db()
        self.assertEqual(self.test_product.name, "Updated Name")
        self.assertEqual(self.test_product.description, "Updated description")
        self.assertEqual(str(self.test_product.price), "2000.00")

    def test_get_product_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "products/products-edit.html")
