from django.test import TestCase


class CartUrlsTests(TestCase):

    def test_view_cart_template(self):
        response = self.client.get('/cart/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
