from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import UserProfile


@receiver(post_save, sender=User)
def create_profile_for_auth_user(sender, instance: User, created: bool, **kwargs) -> None:
    if created:
        UserProfile.objects.create(user=instance)
