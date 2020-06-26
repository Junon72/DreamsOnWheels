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
        'from_email'
    )
    list_filter = (
        'status',
        'date',
    )
    search_fields = (
        'date',
        'subject',
        'message',
        'name',
        'from_email'
    )
    actions = [
        'sales_read',
        'sales_follow',
        'sales_done',
        'contributor_request',
        'contributor_exchange',
        'contributor_done',
        'other_read',
        'other_follow',
        'other_done']

    def sales_read(self, request, queryset):
        quesryset.updtae(status='r')

    def sales_follow(self, request, queryset):
        quesryset.updtae(status='f')

    def sales_done(self, request, queryset):
        quesryset.updtae(status='d')

    def contributor_request(self, request, queryset):
        quesryset.updtae(status='c')

    def contributor_exchange(self, request, queryset):
        quesryset.updtae(status='e')

    def contributor_done(self, request, queryset):
        quesryset.updtae(status='a')

    def other_read(self, request, queryset):
        quesryset.updtae(status='or')

    def other_follow(self, request, queryset):
        quesryset.updtae(status='of')

    def other_done(self, request, queryset):
        quesryset.updtae(status='od')




