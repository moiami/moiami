from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.common.authentication import HeaderUserAuthentication
from api.v1.watchlist.serializers import (
    WatchListAddMovieSerializer,
    WatchListListSerializer,
    WatchListSerializer,
)
from apps.watchlist.models import WatchList
from services.watchlist import WatchlistService


class WatchListViewSet(viewsets.ModelViewSet[WatchList]):
    authentication_classes = [HeaderUserAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return WatchlistService.get_all_watchlists(self.request.user.id)

    def get_serializer_class(self):
        if self.action == "list":
            return WatchListListSerializer
        if self.action == "add_movie":
            return WatchListAddMovieSerializer
        return WatchListSerializer

    def list(self, request, *args, **kwargs):
        """
        Получение списка watchlist'ов текущего пользователя
        GET /api/v1/watchlists
        """
        print(self.request.user.roles, flush=True)

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            response = Response(
                {
                    "count": self.paginator.page.paginator.count,
                    "next": self.paginator.get_next_link(),
                    "previous": self.paginator.get_previous_link(),
                    "watchlists": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

            response["testdfd"] = str(self.request.user.roles)

            return response

        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {"watchlists": serializer.data}, status=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        """
        Создание watchlist'а для текущего пользователя
        POST /api/v1/watchlists
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        watchlist = WatchlistService.create_watchlist(
            name=serializer.validated_data["name"],
            owner_id=self.request.user.id,
        )
        response_serializer = WatchListSerializer(watchlist)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def retrieve(self, request, *args, **kwargs):
        """
        Получение детальной информации по watchlist
        GET /api/v1/watchlists/{id}
        """
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удаление watchlist текущего пользователя
        DELETE /api/v1/watchlists/{id}
        """
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=["post"], url_path="movies")
    def add_movie(self, request, *args, **kwargs):
        """
        Добавление фильма в watchlist
        POST /api/v1/watchlists/{id}/movies
        """
        watchlist = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        WatchlistService.add_movie_to_watchlist(
            watchlist_id=watchlist.id,
            movie_id=serializer.validated_data["movie"].id,
            owner_id=self.request.user.id,
        )
        watchlist = self.get_queryset().get(id=watchlist.id)
        response_serializer = WatchListSerializer(watchlist)

        return Response(
            response_serializer.data,
            status=status.HTTP_200_OK,
        )
