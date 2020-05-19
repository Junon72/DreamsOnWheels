from django.test import TestCase, Client
from django.urls import reverse
from products.models import Original, Vote


class HighlightViewsTest(TestCase):

	def setUp(self):
		self.client = Client()
		self.highlight_url = reverse('highlight:get_highlight', args=['h'])
		self.highlight1 = Original.objects.create(status='h')

	def test_highlight_GET_original_list(self):

		response = self.client.get(self.highlight_url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'highlight.html')

class VoteViewTest(TestCase):

	def setUp(self):
		self.client = Client()
		self.highlight_url_to_vote = reverse('highlight:up_vote', args=[1])
		self.highlight1 = Original.objects.create(id=1)

	def test_highlight_list_GET_original(self):
	
		response = self.client.get(self.highlight_url_to_vote)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'highlight.html')

	# def test_highlight_vote_POST_adds_vote(self):
	# 	Vote.objects.create(
	# 		vote=
	# 	)