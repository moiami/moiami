from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(
    r'movies',
    views.MovieViewSet,
    basename='movie'
)

router.register(
    r'genres-movies',
    views.GenreMovieViewSet,
    basename='genres-movie'
)

router.register(
    r'genres',
    views.GenreViewSet,
    basename='genre'
)

router.register(
    r'images',
    views.ImageViewSet,
    basename='image'
)

router.register(
    r'videos',
    views.VideoViewSet,
    basename='video'
)

# GET /subscriptions/
# GET /subscriptions/{id}/
# GET /subscriptions/{id}/users/
# GET /user-subscriptions/check/{subscription_id}/
# POST /user-subscriptions/add/

urlpatterns = [
    path('', include(router.urls)),
]