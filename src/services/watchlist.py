import uuid

from apps.catalog.models import Movie
from apps.watchlist.models import WatchList


class Watchlist:
    @staticmethod
    def create_watchlist(name: str) -> WatchList:
        return WatchList.objects.create(name=name)

    @staticmethod
    def delete_watchlist(watchlist_id: uuid.UUID) -> bool:
        deleted_count, _ = WatchList.objects.filter(id=watchlist_id).delete()

        # TODO: Тут нужно либо, чтобы
        # a) база сама дропала ватчлисты из пользователя при удалении
        # б) ну чистить у пользователей как-то ее

        return bool(deleted_count)

    @staticmethod
    def add_movie_to_watchlist(
        watchlist_id: uuid.UUID,
        movie_id: uuid.UUID,
    ):
        watchlist = WatchList.objects.get(id=watchlist_id)
        movie = Movie.objects.get(id=movie_id)
        watchlist.movies.add(movie)

    @staticmethod
    def get_all_ids() -> list[uuid.UUID]:
        return list(WatchList.objects.values_list('id', flat=True))

    @staticmethod
    def get_watchlist(watchlist_id: uuid.UUID) -> WatchList:
        """Возвращет WatchList, который содержит кэшированные значения movies"""
        return WatchList.objects.prefetch_related('movies').get(id=watchlist_id)
