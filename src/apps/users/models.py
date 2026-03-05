from django.contrib.auth.models import User as AuthUser
from django.db import models
from django.db.models import (
    ManyToManyField,
    OneToOneField,
)

from apps.watchlist.models import WatchList


class UserProfile(models.Model):
    user = OneToOneField(
        AuthUser,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    watchlists = ManyToManyField(
        WatchList,
        related_name='profiles',
        blank=True,
    )

    def __str__(self) -> str:
        return self.user.username
