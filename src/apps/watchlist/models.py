import uuid

from django.db import models
from django.db.models import (
    CharField,
    ManyToManyField,
    UUIDField,
)

from apps.catalog.models import Movie


class WatchList(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField(max_length=255)
    movies = ManyToManyField(Movie, related_name='watchlists', blank=True)

    def __str__(self):
        return str(self.name) + str(self.id)
