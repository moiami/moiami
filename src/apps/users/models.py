from django.db import models
from django.db.models import DateTimeField, ManyToManyField

from apps.watchlist.models import WatchList

# Create your models here

class User(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = DateTimeField("date published")
    watchlists = ManyToManyField(
        WatchList,
        related_name='users',
        blank=True,
    )
