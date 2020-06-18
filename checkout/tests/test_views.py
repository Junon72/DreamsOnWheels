from django.test import TestCase
from django.shortcuts import reverse, redirect
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from checkout.models import Order, OrderLineItem
from products.models import Product


class CheckoutViewsTests(TestCase):


    def test_get_checkout_response_not_logged_in(self):
        response = self.client.get("/checkout/")
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_get_checkout_response_as_swimmer(self):
            User.objects.create_user(
                username='testuser',
                email='usr@mail.com',
                password='passW0rd')
            self.client.login(username='testuser', password='passW0rd')
            response = self.client.get("/checkout/")
            self.assertEqual(response.status_code, 200)

    def test_card_accepted(self):
        User.objects.create_user(
                username='testuser',
                email='usr@mail.com',
                password='passW0rd')
        self.client.login(username='testuser', password='passW0rd')

        response = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '2',
            'expiry_year': '2023',
            'stripe_id': 'tok_visa'
            }, follow=True)

        for message in get_messages(response.wsgi_request):
            print(message)
            # self.assertEqual(message.tags, "success")
            # self.assertNotEqual("You have successfully paid", messages)

        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)

    def test_card_declined(self):

        User.objects.create_user(
                username='testuser',
                email='usr@mail.com',
                password='passW0rd')
        self.client.login(username='testuser', password='passW0rd')

        response = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '2',
            'expiry_year': '2025',
            'stripe_id': 'tok_chargeDeclined',
            }, follow=True)

        for message in get_messages(response.wsgi_request):
            print(message)
        #     self.assertEqual(messages.tags, "error")
        #     self.assertEqual("Your card was declined!", messages)

        response = self.client.get("/checkout/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout.html")