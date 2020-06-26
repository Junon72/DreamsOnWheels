from django.contrib import admin
from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'contributor', 'phone_number','zipcode', 'country')
    list_filter = ('contributor',)
