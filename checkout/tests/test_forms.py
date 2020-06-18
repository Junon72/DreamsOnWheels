from django.test import TestCase
from checkout.forms import MakePaymentForm, OrderForm
from checkout.models import Order


class TestMakePaymentForm(TestCase):
    def test_make_payment_form(self):
        form = MakePaymentForm({'credit_card_number': '', 'cvv': ''})
        self.assertFalse(form.is_valid())
        form = MakePaymentForm(
            {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '2',
            'expiry_year': '2023',
            'stripe_id': 'tok_visa'
            }
        )
        self.assertTrue(form.is_valid())

class TestOrderForm(TestCase):
    def test_order_form(self):
        form = OrderForm(
            {
            'full_name': 'John Smith',
            'phone_number': '5552424',
            'postcode': '12345'
            }
        )
        self.assertFalse(form.is_valid())
