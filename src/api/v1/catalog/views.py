from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from services import catalog as catalog_service

from api.v1.catalog.serializers import MovieListSerializer,MovieSerializer,GenreMovieSerializer,GenreListSerializer,GenreSerializer,ImageListSerializer,ImageSerializer,VideoListSerializer,VideoSerializer

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для жанров"""

    permission_classes = [AllowAny]

    def get_queryset(self):
        return catalog_service.get_all_genre()

    def get_serializer_class(self):
        if self.action == "list":
            return GenreListSerializer
        return GenreSerializer

    def list(self, request, *args, **kwargs):
        """
        Получение списка фильмов
        GET /api/v1/catalog/genres/
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Получение детальной информации по фильму
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

    def get_queryset(self):
        return catalog_service.get_all_images()

    def get_serializer_class(self):
        if self.action == "list":
            return ImageListSerializer
        return ImageSerializer

    def list(self, request, *args, **kwargs):
        """
        Получение списка фильмов
        GET /api/v1/catalog/images/
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Получение детальной информации по фильму
        GET /api/v1/catalog/images/{id}/
        """
        try:
            movie = self.get_object()
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "Обложка не найдена"},status=status.HTTP_404_NOT_FOUND,)

class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для видео"""

    permission_classes = [AllowAny]

    def get_queryset(self):
        return catalog_service.get_all_videos()

    def get_serializer_class(self):
        if self.action == "list":
            return VideoListSerializer
        return VideoSerializer

    def list(self, request, *args, **kwargs):
        """
        Получение списка фильмов
        GET /api/v1/catalog/videos/
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Получение детальной информации по фильму
        GET /api/v1/catalog/videos/{id}/
        """
        try:
            movie = self.get_object()
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "Видео не найдено"},status=status.HTTP_404_NOT_FOUND,)

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для фильмов"""

    permission_classes = [AllowAny]

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

class GenreMovieViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset для жанров фильма"""

    permission_classes = [AllowAny]

    def get_queryset(self):
        return catalog_service.get_ganre_by_movie_id('')#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return GenreMovieSerializer

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

''' 
class UserSubscriptionViewSet(viewsets.GenericViewSet):
    """Viewset для подписок пользователей"""

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return subscriptions_service.get_user_subscriptions(self.request.user.id)

    def get_serializer_class(self):
        if self.action == "add_subscription":
            return SubscribeSerializer
        return UserSubscriptionSerializer

    @action(detail=False, methods=["post"], url_path="add")
    def add_subscription(self, request):
        """
        Добавление подписки пользователю
        POST /api/v1/user-subscriptions/add/
        Body: {"subscription_id": 1}
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = subscriptions_service.subscribe_user(
                user_id=request.user.id,
                subsciption_id=serializer.validated_data["subscription_id"],
            )

            return Response(
                {
                    "message": "Подписка успешно оформлена",
                    "user_subscription": result,
                },
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=False, methods=["get"], url_path="check/{subscription_id}")
    def check_subscription(self, request, subscription_id=None):
        """
        Проверка наличия определённой подписки у пользователя
        GET /api/v1/user-subscriptions/check/{subscription_id}/
        """
        if not subscription_id:
            return Response(
                {"error": "subscription_id is required"},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            result = subscriptions_service.check_subscription(
                user_id=request
            )

            return Response(
                {
                    "user_id": request.user.id,
                    "subscription_id": subscription_id,
                    "has_subscription": result,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=True, methods=["get"], url_path="users")
    def get_users_with_subscription(self, request, subscription_id=None):
        """
        Получение всех пользователей с определённой подпиской
        GET /api/v1/user-subscriptions/{subscription_id}/users/
        """
        try:
            result = subscriptions_service.get_users_with_subscription(
                subscription_id
            )
            serializer = UsersWithSubscriptionSerializer(result, many=True)

            return Response(
                {
                    "subscription_id": subscription_id,
                    "users_count": len(result),
                    "users": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
'''