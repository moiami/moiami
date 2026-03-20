import django_filters.rest_framework
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
from domain.exeptions import (
    NotFoundGenre,
    NotFoundGenresByMovieId,
    NotFoundImage,
    NotFoundMovie,
    NotFoundMoviesBySubscriptionId,
    NotFoundVideo,
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
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception:
            raise NotFoundGenre()
    def retrieve(self, request, *args, **kwargs):
        """
        Получение информации по жанру
        GET /api/v1/catalog/genres/{id}/
        """
        try:
            movie = self.get_object()
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Exception:
            raise NotFoundGenre()

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
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception:
            raise NotFoundImage()

    def retrieve(self, request, *args, **kwargs):
        try:
            movie = self.get_object()
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Exception:
            raise NotFoundImage()

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
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception:
            raise NotFoundVideo()

    def retrieve(self, request, *args, **kwargs):
        try:
            movie = self.get_object()
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Exception:
            raise NotFoundVideo()

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для фильмов"""

    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields =  ['director','script_writer','age_restriction','date','date_of_premiere','country','genres']
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
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception:
            raise NotFoundMovie()

    def retrieve(self, request, *args, **kwargs):
        """
        Получение детальной информации по фильму
        GET /api/v1/catalog/movies/{id}/
        """
        try:
            movie = self.get_object()
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Exception:
            raise NotFoundMovie()

    @action(detail=True, methods=['get'], url_path='genres')
    def genres(self, request, pk):
        """
        Получить все жанры для конкретного фильма
        GET /api/v1/catalog/movies/{movie_id}/genres/
        """
        try:
            return Response(GenreListSerializer(catalog_service.get_ganre_by_movie_id(id), many=True).data)
        except Exception:
            raise NotFoundGenresByMovieId()

    @action(detail=False,methods=['get'],url_path='subscriptions/<int:subscription_id>')
    def by_subscription(self, request, subscription_id):
        """
        Получить все фильмы по ID подписки
        GET /api/v1/catalog/movies/subscriptions/{subscription_id}/
        """
        try:
            return Response(MovieListSerializer(catalog_service.get_movie_by_subscription_id(subscription_id), many=True).data)
        except Exception:
            raise NotFoundMoviesBySubscriptionId()
