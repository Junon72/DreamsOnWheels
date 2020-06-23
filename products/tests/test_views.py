from django.http import Http404, HttpRequest
from django.shortcuts import get_list_or_404
from django.test import TestCase
from products.models import Product, Original


class TestProductViews(TestCase):

    def test_can_get_original(self):
        o1 = Original.objects.create(make="Original", status='h', id=1)
        o2 = Original.objects.create(make="Automobile", status='a', id=2)
        p1 = Product.objects.create(make="Mobile", original_key=o2)
        originals = get_list_or_404(Original)
        self.assertEqual(
            get_list_or_404(
                Original.objects.all(),
                make__contains="Original"),
                [o1]
            )

    def test_can_get_products(self):
        o1 = Original.objects.create(make="Original", status='h', pk=1)
        o2 = Original.objects.create(make="Automobile", status='a', pk=2)
        Product.objects.create(make="Auto", original_key=o1)
        Product.objects.create(make="Mobile", original_key=o2)
        products = Product.objects.all()
        self.assertEqual(products.count(), 2)
        self.assertEqual(
            get_list_or_404(
                Product.objects.all(),
                make__contains="Mobile"),
                [products[1]]
            )
