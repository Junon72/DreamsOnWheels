from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product, Original
from django.contrib.auth.models import User


class TestProductViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.products_url = reverse('products:all_products')

    def test_get_products_list(self):
        response = self.client.get(self.products_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')

    # def test_