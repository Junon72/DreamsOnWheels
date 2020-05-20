from django.contrib import admin
from .models import *

admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('status', 'owner', 'content', 'post', 'created_date')
    list_filter = ('status', 'created_date')
    search_fields = ('owner', 'content')
    actions = ['approve_comments', 'suspend_comments']
    
    
    def approve_comments(self, request, queryset):
        queryset.update(status='p')
        
    def suspend_comments(self, request, queryset):
        queryset.update(status='s')

