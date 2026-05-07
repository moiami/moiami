from django.db.models import Count, QuerySet

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
        start_timestamp: int,
        end_timestamp: int,
    ) -> int:
        return MovieGetAction.objects.filter(
            movie=movie,
            happened_at__gte=start_timestamp,
            happened_at__lte=end_timestamp,
        ).count()

    @staticmethod
    def get_top_movies_by_views(
        start_timestamp: int,
        end_timestamp: int,
        limit: int,
    ) -> QuerySet[Movie]:
        return (
            Movie.objects.filter(
                get_actions__happened_at__gte=start_timestamp,
                get_actions__happened_at__lte=end_timestamp,
            )
            .annotate(views_count=Count('get_actions'))
            .order_by('-views_count', 'id')[:limit]
        )
