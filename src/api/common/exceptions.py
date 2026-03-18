from rest_framework import status
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from domain import exceptions


def exception_handler(e, context):
    """Единый формат ошибок для API"""

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
