from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product


class CheckoutViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            email='usr@mail.com',
            username='testUser',
            password='passW0rd',
            first_name='Larry',
            last_name='Lentel'
        )

        product = Product.objects.create(
            make='Test Product',
            description='Test Description',
            price=99.99,
        )

    def test_checkout_template(self):
        response = self.client.get('/checkout/')

        self.assertTrue(response.status_code, 200)

    def test_checkout_payment_with_valid_credentials(self):
        self.client.login(email='usr@mail.com', password='passW0rd')
        product = Product.objects.get(id=1)
        response = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '7',
            'expiry_year': '2023',
            'stripe_id': 'tok_visa',
        })

        # self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('products:all_products'), fetch_redirect_response=False)

    def test_checkout_payment_with_declined_card(self):
        self.client.login(email='usr@mail.com', password='passW0rd')
        product = Product.objects.get(id=1)
        response = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '7',
            'expiry_year': '2023',
            'stripe_id': 'tok_chargeDeclined',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('checkout.html')
        self.assertTemplateNotUsed('products.html')
