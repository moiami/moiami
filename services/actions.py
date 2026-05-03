from datetime import datetime

from api.common.authentication import HeaderUser
from apps.actions.models import MovieGetAction
from apps.catalog.models import Movie


class MovieGetActionService:
    @staticmethod
    def create(
        movie: Movie,
        user: HeaderUser | None = None,
    ) -> MovieGetAction:
        return MovieGetAction.objects.create(
            movie=movie,
            user_id=user.id if user is not None else None,
        )

    @staticmethod
    def count_by_movie_and_period(
        movie: Movie,
        start_timestamp: datetime,
        end_timestamp: datetime,
    ) -> int:
        return MovieGetAction.objects.filter(
            movie=movie,
            happened_at__gte=start_timestamp,
            happened_at__lte=end_timestamp,
        ).count()
