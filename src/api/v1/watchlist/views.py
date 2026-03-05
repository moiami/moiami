import json
import uuid

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.http import (
    require_GET,
    require_http_methods,
    require_POST,
)

from apps.users.models import UserProfile
from domain.errors.invalid_json import invalid_json_error
from services.watchlist import Watchlist


def _get_user_profile(request: HttpRequest) -> UserProfile:
    return UserProfile.objects.get(user=request.user)


@require_POST
@login_required
def create_watchlist(request: HttpRequest) -> JsonResponse:
    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return invalid_json_error()

    name = payload.get('name')

    if name is None or len(name.strip()) == 0:
        return JsonResponse({'description': 'Field `name` is required.'}, status=400)

    watchlist = Watchlist.create_watchlist(
        name=name.strip(),
        user_profile=_get_user_profile(request),
    )

    return JsonResponse({'id': str(watchlist.id)}, status=201)


@require_GET
def get_all_watchlists(request: HttpRequest) -> JsonResponse:
    watchlist_ids = Watchlist.get_all_ids()
    data = {'watchlists': [{'id': str(watchlist_id)} for watchlist_id in watchlist_ids]}

    return JsonResponse(data, status=200)


@require_http_methods(['DELETE'])
@login_required
def delete_watchlist(request: HttpRequest, watchlist_id: uuid.UUID) -> HttpResponse:
    is_deleted = Watchlist.delete_watchlist(
        watchlist_id=watchlist_id,
        user_profile=_get_user_profile(request),
    )

    if not is_deleted:
        return JsonResponse({'description': 'Watchlist not found'}, status=404)

    return HttpResponse(status=204)
