from django.test import SimpleTestCase, TestCase, Client
from django.urls import path, reverse, resolve
from products.models import Product, Original
from home.views import index


class TestIndexViews(TestCase):

    def test_get_index_page(self):
        self.original1 = Original.objects.create(pk=1, status='h')
        self.product1 = Product.objects.create(pk=1)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')