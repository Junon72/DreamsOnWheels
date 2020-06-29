from django.test import TestCase, Client
from django.shortcuts import redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, resolve
from products.models import Original, Vote
from django.contrib.auth.models import User


class TestHighlightGetViews(TestCase):
    '''
    Test was build with the help from Code Institute
    tutor Xavier Astor.
    '''

    @classmethod
    def setUpTestData(cls):
        Original.objects.create(
            make="Bluesmobile",
            status='h',
            votes=0
        )
        Original.objects.create(
            make="Automobile",
            status='a',
            votes=0
        )
        Original.objects.create(
            make="Batmobile",
            status='h',
            votes=0
        )

    def test_highlight_GET_original_highlight_list(self):
        self.highlight_url = reverse('highlight:get_highlight')
        highlights = Original.objects.filter(status='h')
        response = self.client.get(self.highlight_url)

        self.assertEqual(highlights.count(), 2)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'highlight.html')

    def test_user_logged_in_POST_vote_request_response(self):
        user = User.objects.create_user(
            username='testUser',
            email='email@test.com',
            password='testWord')
        self.client.force_login(user=user)

        request = self.client.post('/highlight/vote/1/'.format(Original.id))
        self.assertEqual(request.status_code, 302)
        
        response = self.client.get('/highlight/highlight/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'highlight.html')

