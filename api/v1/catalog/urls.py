from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register( r'movies', views.MovieViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'videos', views.VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]