from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

POST_STATUS_CHOICES = [
    ('d', 'Draft'),
    ('r', 'Review'),
    ('p', 'Published')
]

class Post(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=20, default="DOW")
    author_image = models.ImageField(upload_to="img", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    status = models.CharField(max_length=1, choices=POST_STATUS_CHOICES, default='d')
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

COMMENT_STATUS_CHOICES = [
    ('m', 'Moderate'),
    ('p', 'Published'),
    ('s', 'Suspended')
]

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        related_name='comments',
        null=False,
		default=1
    )
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=1, choices=COMMENT_STATUS_CHOICES, default='m')

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.username)