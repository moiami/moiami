from django.http import HttpRequest, JsonResponse
from services.catalog import Catalog

def get_all_movies(request: HttpRequest) -> JsonResponse:
    movies = Catalog.get_all_movies()
    data = {"movies": [{"id": str(movie.id)} for movie in movies]}

    return JsonResponse(data, status=200)


def create_movie(request: HttpRequest) -> JsonResponse:
    movie = Catalog.create_movie()

    return JsonResponse({"id": str(movie.id)}, status=201)
