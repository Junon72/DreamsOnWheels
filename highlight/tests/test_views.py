from django.test import TestCase, Client
from django.shortcuts import redirect, get_list_or_404
from django.urls import reverse, resolve
from products.models import Original, Vote
from django.contrib.auth.models import User


class TestHighlightViews(TestCase):

    def setUp(self):
        self.highlight_url = reverse('highlight:get_highlight')
        o1 = Original.objects.create(
            id=1,
            make="Original",
            status='h',
            votes=0
        )
        o2 = Original.objects.create(
            id=2,
            make="Automobile",
            status='a',
            votes=0
        )

    def test_highlight_GET_original_highlight_list(self):
        highlight = Original.objects.filter(status='h')
        response = self.client.get(self.highlight_url)
        self.assertEqual(highlight.count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'highlight.html')

    def test_user_voting_not_logged_in_is_redirected(self):
        # request = 
        response = self.client.get(self.highlight_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'highlight.html')

        user = User.objects.create_user(
            username='testUser',
            email='email@test.com',
            password='testWord')

    def test_user_logged_in_can_vote(self):
        self.client.force_login(user=user)
        response = self.client.get(self.highlight_url_to_vote)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'highlight.html')

