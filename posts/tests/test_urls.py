from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts.views import get_posts, post_detail, CommentUpdateView, CommentDeleteView


class TestUrls(SimpleTestCase):

    def test_get_posts_url_is_resolved(self):
        url = reverse('posts:get_posts')
        print(resolve(url))
        self.assertEquals(resolve(url).func, get_posts)
