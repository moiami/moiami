import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """Extends Django's built-in User with app-specific fields."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # models.CASCADE => if User object is deleted, UserProfile object will be deleted, too. UserProfile has no meaning without its user.

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f"Profile({self.user.username})"


@receiver(post_save, sender=User)   # only call this function when the sender is User, and only after it's saved (created)
def create_user_profile(sender, instance, created, **kwargs):
    """On new User creation: make a UserProfile."""
    if created:
        UserProfile.objects.create(user=instance)
