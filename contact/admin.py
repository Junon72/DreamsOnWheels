from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'date',
        'subject',
        'message',
        'name',
        'from_email')
    search_fields = ('date', 'subject', 'name', 'from_email')
    actions = ['publish_post', 'draw_post']



