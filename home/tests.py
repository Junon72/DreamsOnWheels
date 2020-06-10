from django.test import TestCase, Client
from django.http import Http404
from django.shortcuts import get_list_or_404, render, redirect, reverse
from .views import *
from products.models import Product, Original


# class TestGetListOfProductsOr404(TestCase):
#     def test_get_list_or_404(self):
#         p1 = Product.objects.create(make="Ford")
#         p2 = Product.objects.create(make="Ford")
        
#         with self.assertRaises(Http404):
#             get_list_or_404(Product.objects.none(), make__contains="Ford")

class TestIndexViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.product_url = reverse('products:all_products', args[1])
        self.product1 = Product.objects.create(pk=1)
        self.original_url = reverse('products:get_original', args=[1])
        self.original1 = Original.objects.create(pk=1)

    def test_get_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

