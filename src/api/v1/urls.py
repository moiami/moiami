from django.urls import path

from api.v1.catalog import views as catalog_views
from api.v1.watchlist import views as watchlist_views

urlpatterns = [
    path("catalog/movies", catalog_views.get_all_movies, name="catalog-get-all-movies"),
    path("catalog/movies/create", catalog_views.create_movie, name="catalog-create-movie"),
    path("watchlists/create", watchlist_views.create_watchlist, name="watchlist-create"),
    path("watchlists/all", watchlist_views.get_all_watchlists, name="watchlist-get-all"),
    path(
        "watchlists/<uuid:watchlist_id>/delete",
        watchlist_views.delete_watchlist,
        name="watchlist-delete",
    ),
]
