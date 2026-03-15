import uuid

from django.db.models import QuerySet

from apps.catalog.models import Movie
from apps.users.models import UserProfile
from apps.watchlist.models import WatchList


class Watchlist:
    @staticmethod
    def create_watchlist(
        name: str,
        user_profile: UserProfile,
    ) -> WatchList:
        watchlist = WatchList.objects.create(name=name)

        user_profile.watchlists.add(watchlist)

        return watchlist

    @staticmethod
    def delete_watchlist(
        watchlist_id: uuid.UUID,
        user_profile: UserProfile,
    ) -> bool:
        deleted_count, _ = user_profile.watchlists.filter(id=watchlist_id).delete()

        return bool(deleted_count)

    @staticmethod
    def add_movie_to_watchlist(
        watchlist_id: uuid.UUID,
        movie_id: uuid.UUID,
        user_profile: UserProfile,
    ) -> None:
        watchlist = user_profile.watchlists.get(id=watchlist_id)
        movie = Movie.objects.get(id=movie_id)

        watchlist.movies.add(movie)

    @staticmethod
    def get_all_ids() -> list[uuid.UUID]:
        return list(WatchList.objects.all().values_list('id', flat=True))

    @staticmethod
    def get_all_watchlists(user_profile: UserProfile) -> QuerySet[WatchList]:
        return user_profile.watchlists.all().prefetch_related('movies')

    @staticmethod
    def get_watchlist(
        watchlist_id: uuid.UUID
    ) -> WatchList:
        """Возвращет WatchList, который содержит кэшированные значения movies"""
        queryset = WatchList.objects.prefetch_related('movies')

        return queryset.get(id=watchlist_id)
