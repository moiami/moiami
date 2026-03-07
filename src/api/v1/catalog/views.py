from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from services import catalog as catalog_service
from api.v1.catalog.serializers import MovieListSerializer,MovieSerializer,GenreMovieSerializer,GenreListSerializer,GenreSerializer,ImageListSerializer,ImageSerializer,VideoListSerializer,VideoSerializer
import django_filters.rest_framework

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для жанров"""

    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]

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
        try:
            movie = self.get_object()
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "Жанр не найден"},status=status.HTTP_404_NOT_FOUND,)

class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для обложек"""

    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]

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
        try:
            movie = self.get_object()
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "Обложка не найдена"},status=status.HTTP_404_NOT_FOUND,)

class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для видео"""

    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]

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
        try:
            movie = self.get_object()
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "Видео не найдено"},status=status.HTTP_404_NOT_FOUND,)

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для фильмов"""

    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields =  ['director','script_writer','age_restriction','date','date_of_premiere','country','genres']

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
        try:
            movie = self.get_object()
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "Фильм не найден"},status=status.HTTP_404_NOT_FOUND,)

    @action(detail=True, methods=['get'], url_path='genres')
    def genres(self, request, pk):
        """
        Получить все жанры для конкретного фильма
        GET /api/v1/catalog/movies/{movie_id}/genres/
        """
        return Response(GenreListSerializer(catalog_service.get_ganre_by_movie_id(id), many=True).data)

    @action(detail=False,methods=['get'],url_path='subscriptions/<int:subscription_id>')
    def by_subscription(self, request, subscription_id):
        """
        Получить все фильмы по ID подписки
        GET /api/v1/catalog/movies/subscriptions/{subscription_id}/
        """
        return Response(MovieListSerializer(catalog_service.get_movie_by_subscription_id(subscription_id), many=True).data)