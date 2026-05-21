from dataclasses import dataclass
from uuid import UUID

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

USER_ID_KEY = "HTTP_X_USER_ID"


@dataclass(frozen=True)
class HeaderUser:
    id: UUID

    @property
    def is_authenticated(self) -> bool:
        return True


class HeaderUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        raw_user_id = request.META.get(USER_ID_KEY)

        if not raw_user_id:
            return None

        try:
            user_id = UUID(raw_user_id)
        except (TypeError, ValueError) as exc:
            raise AuthenticationFailed(
                "X-User-Id header must be a valid UUID"
            ) from exc

        return (HeaderUser(id=user_id), None)
