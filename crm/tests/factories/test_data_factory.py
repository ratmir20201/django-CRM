from django.core.files.uploadedfile import SimpleUploadedFile

from ads.models import Ads
from contracts.models import Contract
from leads.models import Lead
from products.models import Product
from tests.test_utils.auth import LoginRequiredTestsMixin


class TestDataFactory(LoginRequiredTestsMixin):
    __test__ = False

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_product = Product.objects.create(
            name="TestService",
            description="Test description for TestService.",
            price=2000.00,
        )
        cls.test_product_2 = Product.objects.create(
            name="TestService_2",
            description="Test description for TestService_2.",
            price=3000.00,
        )
        cls.test_ad = Ads.objects.create(
            name="TestAd",
            product=cls.test_product,
            channel="Telegram",
            budget=10000.00,
        )
        cls.test_lead = Lead.objects.create(
            first_name="TestFirstName",
            last_name="TestLastName",
            phone="123456789",
            email="test@gmail.com",
            ad=cls.test_ad,
        )
        cls.test_lead_2 = Lead.objects.create(
            first_name="TestFirstName",
            last_name="TestLastName",
            phone="223456789",
            email="test2@gmail.com",
            ad=cls.test_ad,
        )
        cls.contract = Contract.objects.create(
            name="TestContract",
            product=cls.test_product,
            document=SimpleUploadedFile(
                name="test_document.pdf",
                content=b"Dummy content of the PDF file.",
                content_type="application/pdf",
            ),
            start_date="2024-01-01",
            end_date="2025-01-01",
            cost=2500.00,
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.test_product.delete()
        cls.test_product_2.delete()
        cls.test_ad.delete()
        cls.test_lead.delete()
        cls.test_lead_2.delete()
        cls.contract.delete()
