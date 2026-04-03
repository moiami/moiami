from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.v1.catalog.serializers import (
    GenreListSerializer,
    GenreSerializer,
    ImageListSerializer,
    ImageSerializer,
    MovieListSerializer,
    MovieSerializer,
    VideoListSerializer,
    VideoSerializer,
)
from services import catalog as catalog_service


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

    def list(self, request, *args, **kwargs):
        """
        Получение списка жанров
        GET /api/v1/catalog/genres/
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Получение информации по жанру
        GET /api/v1/catalog/genres/{id}/
        """
        genre = self.get_object()
        serializer = self.get_serializer(genre)
        return Response(serializer.data)


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для обложек"""

    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    queryset = catalog_service.get_all_images()

    def get_queryset(self):
        return catalog_service.get_all_images()

    def get_serializer_class(self):
        if self.action == "list":
            return ImageListSerializer
        return ImageSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        image = self.get_object()
        serializer = self.get_serializer(image)
        return Response(serializer.data)


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для видео"""

    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    queryset = catalog_service.get_all_videos()

    def get_queryset(self):
        return catalog_service.get_all_videos()

    def get_serializer_class(self):
        if self.action == "list":
            return VideoListSerializer
        return VideoSerializer

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

    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['director', 'script_writer', 'age_restriction', 'date', 'date_of_premiere', 'country', 'genres']
    queryset = catalog_service.get_all_movies()

    def get_queryset(self):
        return catalog_service.get_all_movies()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer

    def list(self, request, *args, **kwargs):
        """
        Получение списка фильмов
        GET /api/v1/catalog/movies/
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        """
        Получение детальной информации по фильму
        GET /api/v1/catalog/movies/{id}/
        """
        movie = self.get_object()
        serializer = self.get_serializer(movie)
        return Response(serializer.data)


    @action(detail=True, methods=['get'], url_path='genres')
    def genres(self, request, pk):
        """
        Получить все жанры для конкретного фильма
        GET /api/v1/catalog/movies/{movie_id}/genres/
        """
        return Response(GenreListSerializer(catalog_service.get_genre_by_movie_id(id), many=True).data)


    @action(detail=False, methods=['get'], url_path='subscriptions/<int:subscription_id>')
    def by_subscription(self, request, subscription_id):
        """
        Получить все фильмы по ID подписки
        GET /api/v1/catalog/movies/subscriptions/{subscription_id}/
        """
        return Response(
            MovieListSerializer(catalog_service.get_movie_by_subscription_id(subscription_id), many=True).data)
