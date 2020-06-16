from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import all_products, get_original


class TestUrls(SimpleTestCase):

    def test_all_products_url_is_resolved(self):
        url = reverse('products:all_products')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_products)

    def test_get_original_url_is_resolved(self):
        url = reverse('products:get_original', args=[id])
        print(resolve(url))
        self.assertEquals(resolve(url).func, get_original)
