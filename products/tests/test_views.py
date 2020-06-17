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
        
        # self.assertRaises(Http404, get_list_or_404, Product, make="Auto")

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


    # def test_can_get_original(self):

    # def test_get_all_products_template(self):
    #     response = self.client.get('/products/')

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed('products.html')

    # def test_get_original_template(self):
    #     # original = Original.objects.get(id=1)
    #     response = self.client.get('/products/original/{0}'.format(o1.id))

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(original.make, 'Original')
    #     self.assertTemplateUsed('original.html')
