from django.test import TestCase, Client
from django.shortcuts import redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, resolve
from products.models import Original, Vote
from django.contrib.auth.models import User


class TestHighlightGetViews(TestCase):

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

# class UserCanVote(TestCase):

#     def test_vote_highlight_vote_is_counted(self):
#         user = User.objects.create_user(
#             id=3,
#             username='testUser',
#             email='email@test.com',
#             password='testWord'
#         )

#         highlight = Original.objects.create(
#             id=1,
#             make="Bluesmobile",
#             status='h',
#             votes=0
#         )

#         self.client.login(username='testUser', password='testWord')
#         print(user)
#         request = self.client.post('/highlight/vote/1/'.format(Original.id))
#         self.assertEqual(Original.objects.count(), 1)
#         Vote.objects.create(user_id=3, highlight_id=1)
#         highlight = Original.objects.get(id=1)
#         self.assertEqual(highlight.votes, 1)
