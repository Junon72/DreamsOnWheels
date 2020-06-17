from django.http import Http404, HttpRequest
from django.shortcuts import get_list_or_404
from django.test import TestCase
from products.models import Original, Product


class GetObjectsOr404Tests(TestCase):

    def test_get_product_or_404(self):
        o1 = Original.objects.create(make="Original", status='h')
        o2 = Original.objects.create(make="Automobile", status='a')
        highlight = Original.objects.filter(status='h')

        self.assertRaises(Http404, get_list_or_404, Product, make="Auto")
        self.assertEqual(highlight.count(), 1)

        p1 = Product.objects.create(make="Auto")
        p2 = Product.objects.create(make="Mobile")
        products = get_list_or_404(Product)

        self.assertEqual(products.count(p1), 1)
        self.assertEqual(
            get_list_or_404(
                Product.objects.all(),
                make__contains="Mobile"),
                [p2]
            )
