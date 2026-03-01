import uuid

from django.db import models


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Genre(models.Model):
    pass

class Video(models.Model):
    pass

class Image(models.Model):
    pass
