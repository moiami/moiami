import uuid
from django.db import models
from watchlist.models import WatchList 
from subscription.models import UserSubscription

from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    IntegerField,
    ManyToManyField,
    OneToOneField,
    TextField,
    URLField,
    UUIDField,
)

class User(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=26)
    password = models.CharField(max_length=128)  # Django hashes are typically 128 chars
    isAdmin = models.BooleanField(default=False)
    watchlists = ManyToManyField(WatchList, related_name='watchlists', blank=True)
    subscriptions = ManyToManyField(UserSubscription, related_name='subscriptions', blank=True)

    def __str__(self):
        return str(self.name) + str(self.id)
