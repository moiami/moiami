import uuid

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import parsers, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.common.authentication import HeaderUser, HeaderUserAuthentication
from api.v1.catalog.serializers import (
    GenreListSerializer,
    GenreSerializer,
    ImageListSerializer,
    ImageSerializer,
    MovieCreateSerializer,
    MovieListSerializer,
    MovieSerializer,
    MovieStatisticsQuerySerializer,
    TopMovieListSerializer,
    TopMoviesQuerySerializer,
    VideoListSerializer,
    VideoSerializer,
)
from apps.catalog.models import Video
from domain import exceptions as domain_exceptions
from services import catalog as catalog_service
from services.actions import MovieGetActionService


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для жанров"""

    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    queryset = catalog_service.get_all_genre()

    def get_queryset(self):
        return catalog_service.get_all_genre()

    def get_serializer_class(self):
        if self.action == "list":
            return GenreListSerializer
        return GenreSerializer

    def create(self, request, *args, **kwargs):
        """
        Создание нового жанра.
        POST /api/v1/catalog/genres/
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        genre = serializer.save()
        return Response(
            GenreSerializer(genre).data,
            status=status.HTTP_201_CREATED,
            headers={"Location": f"/api/v1/catalog/genres/{genre.id}/"},
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        genre = self.get_object()
        serializer = self.get_serializer(genre)
        return Response(serializer.data)


class ImageViewSet(viewsets.ModelViewSet):
    """Viewset для обложек"""

    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    parser_classes = [
        parsers.MultiPartParser,
        parsers.FormParser,
        parsers.JSONParser,
    ]
    queryset = catalog_service.get_all_images()

    def get_queryset(self):
        return catalog_service.get_all_images()

    def get_serializer_class(self):
        if self.action == "list":
            return ImageListSerializer
        return ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = serializer.save()
        return Response(
            ImageSerializer(image).data,
            status=status.HTTP_201_CREATED,
            headers={"Location": f"/api/v1/catalog/images/{image.id}/"},
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        image = self.get_object()
        serializer = self.get_serializer(image)
        return Response(serializer.data)


class VideoViewSet(viewsets.ModelViewSet):
    """Viewset для видео"""

    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    parser_classes = [
        parsers.MultiPartParser,
        parsers.FormParser,
        parsers.JSONParser,
    ]
    queryset = Video.objects.all()

    def get_queryset(self):
        return catalog_service.get_all_videos()

    def get_serializer_class(self):
        if self.action == "list":
            return VideoListSerializer
        return VideoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        video = serializer.save()
        return Response(
            VideoSerializer(video).data,
            status=status.HTTP_201_CREATED,
            headers={"Location": f"/api/v1/catalog/videos/{video.id}/"},
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        video = self.get_object()
        serializer = self.get_serializer(video)
        return Response(serializer.data)


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для фильмов"""

    authentication_classes = [HeaderUserAuthentication]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "director",
        "script_writer",
        "age_restriction",
        "date",
        "date_of_premiere",
        "country",
        "genres",
    ]
    queryset = catalog_service.get_all_movies()

    def get_queryset(self):
        return catalog_service.get_all_movies()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "create":
            return MovieCreateSerializer
        return MovieSerializer

    def create(self, request, *args, **kwargs):
        """
        Создание нового фильма.
        POST /api/v1/catalog/movies/
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = serializer.save()
        return Response(
            MovieSerializer(movie).data,
            status=status.HTTP_201_CREATED,
            headers={"Location": f"/api/v1/catalog/movies/{movie.id}/"},
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        movie = self.get_object()
        user = request.user if isinstance(request.user, HeaderUser) else None
        MovieGetActionService.create(movie=movie, user=user)
        serializer = self.get_serializer(movie)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["get"],
        url_path="film_statistics",
        permission_classes=[AllowAny],
    )
    def film_statistics(self, request, pk=None):
        movie = self.get_object()
        query_serializer = MovieStatisticsQuerySerializer(
            data=request.query_params
        )
        query_serializer.is_valid(raise_exception=True)

        start_timestamp = query_serializer.validated_data["start_timestamp"]
        end_timestamp = query_serializer.validated_data["end_timestamp"]

        views_count = MovieGetActionService.count_by_movie_and_period(
            movie=movie,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
        )
        return Response({"views_count": views_count})

    @action(
        detail=False,
        methods=["get"],
        url_path="top",
        permission_classes=[AllowAny],
    )
    def top(self, request):
        query_serializer = TopMoviesQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)

        start_timestamp = query_serializer.validated_data["start_timestamp"]
        end_timestamp = query_serializer.validated_data["end_timestamp"]
        limit = query_serializer.validated_data["limit"]

        movies = MovieGetActionService.get_top_movies_by_views(
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            limit=limit,
        )
        serializer = TopMovieListSerializer(movies, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="genres")
    def genres(self, request, pk):
        genres_queryset = catalog_service.get_genre_by_movie_id(pk)
        return Response(GenreListSerializer(genres_queryset, many=True).data)

    @action(
        detail=False,
        methods=["get"],
        url_path="subscriptions/<uuid:subscription_id>",
    )
    def by_subscription(self, request, subscription_id):
        """Получить все фильмы по ID подписки"""
        if not isinstance(subscription_id, uuid.UUID):
            subscription_id = uuid.UUID(subscription_id)

        movies = catalog_service.get_movie_by_subscription_id(subscription_id)

        if not movies.exists():
            raise domain_exceptions.NotFoundMoviesBySubscriptionId()

        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
