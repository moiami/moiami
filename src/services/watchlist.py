import uuid

from apps.catalog.models import Movie
from apps.users.models import User
from apps.watchlist.models import WatchList


class Watchlist:
    @staticmethod
    def create_watchlist(
        name: str,
        user: User,
    ) -> WatchList:
        watchlist = WatchList.objects.create(name=name)

        user.watchlists.add(watchlist)

        return watchlist

    @staticmethod
    def delete_watchlist(
        watchlist_id: uuid.UUID,
        user: User,
    ) -> bool:
        deleted_count, _ = user.watchlists.filter(id=watchlist_id).delete()

        return bool(deleted_count)

    @staticmethod
    def add_movie_to_watchlist(
        watchlist_id: uuid.UUID,
        movie_id: uuid.UUID,
        user: User,
    ) -> None:
        watchlist = user.watchlists.get(id=watchlist_id)
        movie = Movie.objects.get(id=movie_id)

        watchlist.movies.add(movie)

    @staticmethod
    def get_all_ids() -> list[uuid.UUID]:
        return list(WatchList.objects.all().values_list('id', flat=True))

    @staticmethod
    def get_watchlist(
        watchlist_id: uuid.UUID
    ) -> WatchList:
        """Возвращет WatchList, который содержит кэшированные значения movies"""
        queryset = WatchList.objects.prefetch_related('movies')

        return queryset.get(id=watchlist_id)
