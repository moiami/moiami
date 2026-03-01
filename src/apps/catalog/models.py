import uuid

from django.db import models
from django.db.models import UUIDField, TextField, DateField, IntegerField, URLField, ManyToManyField, \
    CASCADE, CharField, OneToOneField

from src.apps.subscription.models import Subscription

class Genre(models.Model):
    id = UUIDField(primary_key=True,default=uuid.uuid4)
    name = CharField(max_length=255)
    def __str__(self):
        return str(self.id)

class Video(models.Model):
    id = UUIDField(primary_key=True,default=uuid.uuid4)
    link360 = URLField()
    link1080 = URLField()
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