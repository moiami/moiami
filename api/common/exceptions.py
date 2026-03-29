from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler

from domain import exceptions


def exception_handler(e, context):
    """Единый формат ошибок для API"""

    if isinstance(e, exceptions.NotFoundMoviesBySubscriptionId):
        return Response(
            {
                "error": {
                    "code": "movie_not_found",
                    "message": str(e),
                }
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if isinstance(e, exceptions.NotFoundGenresByMovieId):
        return Response(
            {
                "error": {
                    "code": "genres_not_found",
                    "message": str(e),
                }
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if isinstance(e, exceptions.NotFoundMovie):
        return Response(
            {
                "error": {
                    "code": "movie_not_found",
                    "message": str(e),
                }
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if isinstance(e, exceptions.NotFoundVideo):
        return Response(
            {
                "error": {
                    "code": "video_not_found",
                    "message": str(e),
                }
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if isinstance(e, exceptions.NotFoundImage):
        return Response(
            {
                "error": {
                    "code": "image_not_found",
                    "message": str(e),
                }
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if isinstance(e, exceptions.NotFoundGenre):
        return Response(
            {
                "error": {
                    "code": "genre_not_found",
                    "message": str(e),
                }
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if isinstance(e, exceptions.SubscriptionNotFound):
        return Response(
            {
                "error": {
                    "code": "subscription_not_found",
                    "message": str(e),
                }
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if isinstance(e, exceptions.PermissionDenied):
        return Response(
            {
                "error": {
                    "code": "permission_denied",
                    "message": str(e),
                }
            },
            status=status.HTTP_403_FORBIDDEN,
        )

    response = drf_exception_handler(e, context)
    if response:
        response.data = {
            "error": {
                "code": "api_error",
                "message": str(response.data.get("detail", response.data))
            }
        }

    return response
