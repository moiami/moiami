import uuid

from django.db.models import QuerySet

from apps.catalog.models import Movie, Genre, Video, Image

def get_movie(movie_id: uuid.UUID | str) -> Movie:
    return Movie.objects.get(id=movie_id)

def create_movie() -> Movie:
    return Movie.objects.create()

def get_all_movies() -> QuerySet[Movie]:
    return Movie.objects.all()

def get_ganre_by_movie_id(movie_id: uuid.UUID) -> QuerySet[Genre]:
    return Movie.objects.get(id=movie_id).genres

def get_all_genre() -> QuerySet[Genre]:
    return Genre.objects.all()

def get_all_videos() -> QuerySet[Video]:
    return Video.objects.all()

def get_all_images() -> QuerySet[Image, Image]:
    return Image.objects.all()

def get_movie_by_subscription_id(subscription_id: uuid.UUID) -> QuerySet[Movie]:
    return Movie.objects.filter(subscriptions__id=subscription_id)