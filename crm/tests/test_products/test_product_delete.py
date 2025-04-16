from http import HTTPStatus

from django.urls import reverse

from products.models import Product
from tests.factories.test_data_factory import TestDataFactory


class ProductDeleteViewTestCase(TestDataFactory):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("products:product_delete", kwargs={"pk": cls.test_product.pk})

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_product_delete(self):
        response = self.client.post(self.url)

        self.assertRedirects(response, reverse("products:products_list"))
        self.assertFalse(Product.objects.filter(pk=self.test_product.pk).exists())

    def test_get_product_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "products/products-delete.html")
