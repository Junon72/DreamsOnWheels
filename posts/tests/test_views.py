from django.test import TestCase, Client
from django.urls import reverse
from posts.models import Post, Comment
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testUser',
            email='testUser@mail.com',
            password='Apassword0'
        )
        self.posts_url = reverse('posts:get_posts')
        self.detail_url = reverse('posts:post_detail', kwargs={'pk': 1})
        self.post = Post.objects.create(
            title='Test post 1',
            content='Test post content',
            author=self.user
        )
        self.comment = Comment.objects.create(
            pk=1,
            post=self.post,
            owner=self.user,
            content='Test comment'
        )

    def test_get_posts(self):
        response = self.client.get(self.posts_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogposts.html')

    def test_get_post_detail(self):
        self.assertEqual(Post.objects.count(), 1)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postdetail.html')


    def test_add_new_comment(self):
        self.client.force_login(user=self.user)
        post = Post.objects.get(pk=1)
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.get(pk=1)
        response = self.client.post('/posts/post/')

        self.assertEqual(post.title, 'Test post 1')
        self.assertEqual(comment.content, 'Test comment')

    def test_edit_comment(self):
        self.client.force_login(user=self.user)
        post = Post.objects.get(pk=1)
        comment = Comment.objects.get(pk=1)
        comment.content = 'Edit test comment'
        response = self.client.get('/posts/post/1/update/{0}/'.format(comment.pk))

        self.assertEqual(comment.content, 'Edit test comment')
        self.assertTemplateUsed('edit_comment.html')
