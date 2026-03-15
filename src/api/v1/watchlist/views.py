from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.watchlist.serializers import (
    WatchListListSerializer,
    WatchListSerializer,
)
from apps.users.models import UserProfile
from services.watchlist import Watchlist


class WatchListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def _get_user_profile(self) -> UserProfile:
        return UserProfile.objects.get(user=self.request.user)

    def get_queryset(self):
        return Watchlist.get_all_watchlists(self._get_user_profile())

    def get_serializer_class(self):
        if self.action == 'list':
            return WatchListListSerializer
        return WatchListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response({'watchlists': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        watchlist = Watchlist.create_watchlist(
            name=serializer.validated_data['name'],
            user_profile=self._get_user_profile(),
        )
        response_serializer = WatchListSerializer(watchlist)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )
