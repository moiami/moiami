import pathlib
import uuid

from django.conf import settings
from django.db import models
from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    FileField,
    IntegerField,
    ManyToManyField,
    OneToOneField,
    TextField,
    URLField,
    UUIDField,
)

from apps.subscription.models import Subscription
from services.s3 import generate_presigned_url


def video_upload_path(instance, filename):
    ext = pathlib.Path(filename).suffix.lower()
    quality = instance.quality or 'unknown'
    return f"{quality}/{uuid.uuid4().hex}{ext}"

class Genre(models.Model):
    id = UUIDField(primary_key=True,default=uuid.uuid4)
    name = CharField(max_length=255)
    def __str__(self):
        return str(self.id)


class Video(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)

    QUALITY_CHOICES = [
        ('360', '360p'),
        ('1080', '1080p'),
    ]
    quality = CharField(max_length=10, choices=QUALITY_CHOICES)

    file = FileField(
        upload_to=video_upload_path,
        max_length=500,
        storage=settings.VIDEO_STORAGE,
        null=True,
        blank=True
    )

    @property
    def link(self):
        if not self.file:
            return None
        if getattr(settings, 'AWS_QUERYSTRING_AUTH', False) is False:
            return self.file.url
        return generate_presigned_url(
            self.file.name,
            expiration=3600
        )

    @property
    def link360(self):
        return self.link if self.quality == '360' else None

    @property
    def link1080(self):
        return self.link if self.quality == '1080' else None

    def __str__(self):
        return str(self.id)


class Image(models.Model):
    id = UUIDField(primary_key=True,default=uuid.uuid4)
    link = URLField()
    def __str__(self):
        return str(self.id)

class Movie(models.Model):
    id = UUIDField(primary_key=True,default=uuid.uuid4)
    name = CharField(max_length=255)
    description = TextField()
    director = CharField(max_length=255)
    script_writer = CharField(max_length=255)
    age_restriction = IntegerField()
    date = DateField()
    date_of_premiere = DateField(null=True,blank=True)
    country = CharField(max_length=255)
    genres = ManyToManyField(Genre, related_name='movies')
    subscriptions = ManyToManyField(Subscription, related_name='movies')
    video = OneToOneField(Video, on_delete=CASCADE)
    poster = OneToOneField(Image, on_delete=CASCADE)
    def __str__(self):
        return str(self.id)
