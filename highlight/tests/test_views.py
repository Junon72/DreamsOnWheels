from django.test import TestCase, Client
from django.shortcuts import redirect
from django.urls import reverse, resolve
from products.models import Original, Vote
from django.contrib.auth.models import User


class TestHighlightViews(TestCase):

    def setUp(self):
        self.highlight_url = reverse('highlight:get_highlight')
        self.highlight_url_to_vote = reverse('highlight:get_vote', args=[id])
        highlight = Original.objects.create(
            id=1,
            status='h',
            votes=0
        )
        highlight.save()

    def test_highlight_GET_original_list(self):

        response = self.client.get(self.highlight_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'highlight.html')

    def test_user_voting_not_logged_in_is_redirected(self):
        response = self.client.get(redirect('/highlight/highlight/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'highlight.html')

        user = User.objects.create_user(
            username='testUser',
            email='email@test.com',
            password='testWord')

    def test_user_logged_in_can_vote(self):
        response = self.client.get(self.highlight_url_to_vote)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'highlight.html')

