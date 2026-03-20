from django.test import TestCase

from services.catalog import Catalog


class CatalogTests(TestCase):
    def test_get_all_movies_returns_all_movies(self) -> None:
        movie_1 = Catalog.create_movie()
        movie_2 = Catalog.create_movie()

        movies = Catalog.get_all_movies()
        movie_ids = {movie.id for movie in movies}

        self.assertEqual(movie_ids, {movie_1.id, movie_2.id})

    def test_get_all_movies_endpoint_returns_all_movies(self) -> None:
        movie_1 = Catalog.create_movie()
        movie_2 = Catalog.create_movie()

        response = self.client.get("/api/v1/catalog/movies")

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        movie_ids = {movie["id"] for movie in payload["movies"]}

        self.assertEqual(movie_ids, {str(movie_1.id), str(movie_2.id)})
