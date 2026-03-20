from rest_framework import filters, mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.v1.users.serializers import (
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer,
    UserSubscriptionSerializer,
    WatchListSerializer,
)

from services.users import get_users, get_subscriptions, get_watchlists


# Set of views
class UserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,  # fetching a single object
    viewsets.GenericViewSet,    # About mixins: we could use single inheritance from "viewsets.ModelViewSet", which gives all the CRUD, but we don't need U and D, so we use separate mixins.
):
    queryset = get_users()
    
    """
    The following 3 lines gives our endpoint 2 query params:
    GET /api/v1/users/?search=slava - filters by username or email containing "john"
    GET /api/v1/users/?ordering=username - sorts results by username
    """
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fields = ['date_joined', 'username']

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserListSerializer

    """
    List, Retrieve - are standard endpoints, we don't override them
    Create is alsostandard, but we override it because the default
    would respond with UserCreateSerializer data - we want to respond with full user detail instead
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) # instantiates the UserCreateSerializer object
        serializer.is_valid(raise_exception=True)           # Returns 400 in case of error
        user = serializer.save()                            # calls UserCreateSerializer.create(), which hashes password and saves to DB
        return Response(
            UserDetailSerializer(user).data,
            status=status.HTTP_201_CREATED,     # 201 - "resource was created"
        )

    # detail=True => handles single object
    @action(detail=True, methods=['get'], url_path='subscriptions')
    def subscriptions(self, request, pk=None):  # pk - primary key. Usually ID is put in it.
        user = self.get_object()
        qs = get_subscriptions(user)  # queryset
        return Response(UserSubscriptionSerializer(qs, many=True).data)

    @action(detail=True, methods=['get'], url_path='watchlists')
    def watchlists(self, request, pk=None):
        user = self.get_object()
        qs = get_watchlists(user)
        return Response(WatchListSerializer(qs, many=True).data)