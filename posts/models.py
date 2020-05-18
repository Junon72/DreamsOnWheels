from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=20, default="DOW  ")
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return self.title

