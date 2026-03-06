import uuid

from django.db.models import QuerySet

from apps.catalog.models import Movie,Genre,Video

def get_movie(movie_id: uuid.UUID | str) -> Movie:
    return Movie.objects.get(id=movie_id)

def create_movie() -> Movie:
    return Movie.objects.create()

def get_all_movies() -> QuerySet[Movie]:
    return Movie.objects.all()

def get_ganre_by_movie_id(movie_id: uuid.UUID | str) -> Genre:
    pass

def get_all_genre() -> QuerySet[Genre]:
    pass

def get_all_videos() -> QuerySet[Video]:
    pass

def get_all_images() -> QuerySet[Movie]:
    pass