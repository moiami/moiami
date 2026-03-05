from django.http import JsonResponse


def not_authenticated_error() -> JsonResponse:
    return JsonResponse(
        {'description': 'Not authenticated'},
        status=401,
    )
