import uuid

from django.core.exceptions import ValidationError
from django.db.models import QuerySet

from apps.catalog.models import Genre, Image, Movie, Video
from domain.exceptions import (
    NotFoundGenresByMovieId,
    NotFoundMovie,
)


def get_movie(movie_id: uuid.UUID | str) -> Movie:
    movie = Movie.objects.get(id=movie_id)
    if not movie:
        raise NotFoundMovie()
    return movie


def get_all_movies() -> QuerySet[Movie]:
    return Movie.objects.all()


def get_genre_by_movie_id(movie_id: uuid.UUID) -> QuerySet[Genre]:
    try:
        movie = Movie.objects.get(id=movie_id)
    except (Movie.DoesNotExist, ValidationError, ValueError):
        raise NotFoundGenresByMovieId()

    return movie.genres.all()


def get_all_genre() -> QuerySet[Genre]:
    return Genre.objects.all()


def get_all_videos() -> QuerySet[Video]:
    return Video.objects.all()


def get_all_images() -> QuerySet[Image, Image]:
    return Image.objects.all()


def get_movie_by_subscription_id(subscription_id: uuid.UUID) -> QuerySet[Movie]:
    return Movie.objects.filter(subscriptions__id=subscription_id)