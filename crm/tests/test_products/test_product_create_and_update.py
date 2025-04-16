from http import HTTPStatus

from django.urls import reverse

from products.models import Product
from tests.factories.test_data_factory import TestDataFactory


class ProductCreateViewTestCase(TestDataFactory):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("products:product_create")

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_product_create(self):
        data = {
            "name": "TestServiceCreate",
            "description": "Test description for TestServiceCreate.",
            "price": "1000.00",
        }
        response = self.client.post(path=self.url, data=data)

        self.assertRedirects(response, reverse("products:products_list"))
        self.assertTrue(
            Product.objects.filter(
                name=data["name"],
                description=data["description"],
                price=data["price"],
            ).exists()
        )

    def test_get_product_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "products/products-create.html")


class ProductUpdateViewTestCase(TestDataFactory):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("products:product_update", kwargs={"pk": cls.test_product.pk})

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_product_update(self):
        new_data = {
            "name": "UpdatedService",
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
        self.assertEqual(self.test_product.name, new_data["name"])
        self.assertEqual(self.test_product.description, new_data["description"])
        self.assertEqual(str(self.test_product.price), new_data["price"])

    def test_get_product_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "products/products-edit.html")
