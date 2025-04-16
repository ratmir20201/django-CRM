from http import HTTPStatus

from django.urls import reverse

from products.models import Product
from tests.factories.test_data_factory import TestDataFactory


class ProductsListViewTestCase(TestDataFactory):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("products:products_list")

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_products_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        products = Product.objects.all()
        products_ = response.context["products"]
        for p, p_ in zip(products, products_):
            self.assertEqual(p.pk, p_.pk)

        self.assertTemplateUsed(response, "products/products-list.html")


class ProductDetailViewTestCase(TestDataFactory):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse("products:product_detail", kwargs={"pk": cls.test_product.pk})

    def test_redirect_to_login_if_not_logged_in(self):
        self.assert_login_required()

    def test_product_detail(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "products/products-detail.html")

        self.assertContains(response, self.test_product.name)
        self.assertContains(response, self.test_product.price)
