from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import login, logout, register, user_profile


class TestUrls(SimpleTestCase):
    
    def test_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))