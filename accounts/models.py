from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Profile model for user to create a user profile."""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        default=None,
        related_name="profiles"
    )
    contributor = models.BooleanField(default=False)
    image = models.ImageField(upload_to="avatars/", blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address1 = models.CharField(max_length=95, blank=False)
    address2 = models.CharField(max_length=95, blank=True)
    town_or_city = models.CharField(max_length=80, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=False)
    country = CountryField()

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profiles.save()
