from django.test import TestCase
from contact.forms import ContactForm


class TestContactForms(TestCase):

    def test_valid_contact_form(self):
        form = ContactForm({
            'name': 'Larry Lentel',
            'from_email': 'test@mail.com',
            'subject': 'Test subject',
            'message': 'Test message',
        })

        self.assertTrue(form.is_valid())

    def test_invalid_contact_form(self):
        form = ContactForm({
            'name': 'Larry Lentel',
            'subject': 'Test subject',
            'message': 'Test message',
        })

        self.assertFalse(form.is_valid())
