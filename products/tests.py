from django.test import TestCase, Client
from django.urls import reverse
from .models import Original, Product


class ProductsViewsTest(TestCase):

	def setUp(self):
		self.client = Client()
		self.all_products_url = reverse('products:all_products')
		self.original_url = reverse('products:get_original', args=[1])
		self.original1 = Original.objects.create(pk=1)

	def test_products_GET_all(self):

		response = self.client.get(self.all_products_url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'products.html')

	def test_original_list_GET(self):

		response = self.client.get(self.original_url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'original.html')


