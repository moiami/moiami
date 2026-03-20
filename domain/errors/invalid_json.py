from django.http import JsonResponse


def invalid_json_error() -> JsonResponse:
    return JsonResponse(
        {'description': 'Invalid JSON'},
        status=400,
    )
