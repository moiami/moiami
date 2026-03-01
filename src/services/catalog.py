import uuid
from django.db.models import QuerySet

from apps.catalog.models import Movie

class Catalog:
    @staticmethod
    def get_movie(movie_id: uuid.UUID | str) -> Movie:
        return Movie.objects.get(id=movie_id)
    
    @staticmethod
    def create_movie() -> Movie:
        return Movie.objects.create()

    @staticmethod
    def get_all_movies() -> QuerySet[Movie]:
        return Movie.objects.all()
