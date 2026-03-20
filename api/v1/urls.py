from django.urls import include, path

from api.v1.catalog import views as catalog_views

urlpatterns = [
    path("catalog/movies", catalog_views.get_all_movies, name="catalog-get-all-movies"),
    path("catalog/movies/create", catalog_views.create_movie, name="catalog-create-movie"),
    path('', include('api.v1.watchlist.urls')),
]
