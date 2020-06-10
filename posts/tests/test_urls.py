from django.test import SimpleTestCase
from django.urls import path, reverse, resolve
from posts.views import get_posts, post_detail, CommentUpdateView, CommentDeleteView


class TestUrls(SimpleTestCase):
    
    
    def test_get_posts_url_is_resolved(self):
        url = reverse('posts:get_posts')
        print(resolve(url))
        self.assertEquals(resolve(url).func, get_posts)

    # def test_post_detail_url_is_resolved(self):
    #     post = Post.objects.create(title='Test post detail title',
    #                                 content = 'Test post detail content')
    #     self.assertEqual(Post.objects.count(), 1)
        
    #     url = reverse(
    #         'posts:post_detail', 
    #         args={
    #             'pk': 1
    #             })
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, post_detail)

    # def test_update_comment_url_is_resolved(self):
    #     url = reverse('posts:update', args=[pk])
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func.view_class, CommentUpdateView)

    # def test_delete_comment_url_is_resolved(self):
    #     url = reverse('posts:update', args=[pk])
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func.view_class, CommentDeleteView)