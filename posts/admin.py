from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('status', 'author', 'title', 'created_date', 'tag')
    list_filter = ('status', 'published_date', 'tag')
    search_fields = ('status', 'author')
    actions = ['publish_post', 'draw_post']

    def publish_post(self, request, queryset):
        queryset.update(status='p')

    def draw_post(self, request, queryset):
        queryset.update(status='x')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'owner',
        'content',
        'post',
        'created_date'
    )
    list_filter = ('status', 'created_date')
    search_fields = ('owner', 'content')
    actions = ['approve_comments', 'suspend_comments']

    def approve_comments(self, request, queryset):
        queryset.update(status='p')

    def suspend_comments(self, request, queryset):
        queryset.update(status='s')
