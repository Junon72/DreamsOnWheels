
from django.test import TestCase
# from contact.forms import ContactForm


class TestContactViews(TestCase):

    def test_contact_template(self):
        response = self.client.get('/contact/contact/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('contact.html')

    def test_contact_post_method(self):
        response = self.client.post('/contact/contact/', {
            'name': 'Larry Lentel',
            'from_email': 'test@mail.com',
            'subject': 'Test subject',
            'message': 'Test message',
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/contact/contact/')
