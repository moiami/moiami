import uuid

from django.db.models import QuerySet

from apps.catalog.models import Movie
from apps.watchlist.models import WatchList


class WatchlistService:
    @staticmethod
    def create_watchlist(
        name: str,
        owner_id: uuid.UUID,
    ) -> WatchList:
        return WatchList.objects.create(name=name, owner_id=owner_id)

    @staticmethod
    def delete_watchlist(
        watchlist_id: uuid.UUID,
        owner_id: uuid.UUID,
    ) -> bool:
        deleted_count, _ = WatchList.objects.filter(
            id=watchlist_id,
            owner_id=owner_id,
        ).delete()

        return bool(deleted_count)

    @staticmethod
    def add_movie_to_watchlist(
        watchlist_id: uuid.UUID,
        movie_id: uuid.UUID,
        owner_id: uuid.UUID,
    ) -> None:
        watchlist = WatchList.objects.get(id=watchlist_id, owner_id=owner_id)
        movie = Movie.objects.get(id=movie_id)

        watchlist.movies.add(movie)

    @staticmethod
    def get_all_ids() -> list[uuid.UUID]:
        return list(WatchList.objects.all().values_list("id", flat=True))

    @staticmethod
    def get_all_watchlists(owner_id: uuid.UUID) -> QuerySet[WatchList]:
        return (
            WatchList.objects.filter(owner_id=owner_id)
            .order_by("id")
            .prefetch_related("movies")
        )

    @staticmethod
    def get_watchlist(watchlist_id: uuid.UUID) -> WatchList:
        """Возвращет WatchList, который содержит кэшированные значения movies"""
        queryset = WatchList.objects.prefetch_related("movies")

        return queryset.get(id=watchlist_id)
