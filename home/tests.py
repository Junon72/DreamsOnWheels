from django.test import TestCase
from django.shortcuts import render, redirect, reverse
from .views import *



class TestIndexViews(TestCase):

    def test_get_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
