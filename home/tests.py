from django.test import TestCase
from django.shortcuts import render, redirect, reverse
from .views import *
from products.models import Product, Original



class TestIndexViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.original_url = reverse('products:get_original', args=[1])
        self.original1 = Original.objects.create(pk=1)

    def test_get_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

