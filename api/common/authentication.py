import ast
import json
from dataclasses import dataclass
from uuid import UUID

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

USER_ID_KEY = "HTTP_X_USER_ID"
USER_ROLE_KEY = "HTTP_X_USER_ROLE"


@dataclass(frozen=True)
class HeaderUser:
    id: UUID
    roles: list[str]

    @property
    def is_authenticated(self) -> bool:
        return True


class HeaderUserAuthentication(BaseAuthentication):
    @staticmethod
    def _parse_roles(raw_user_roles: str | None) -> list[str]:
        if raw_user_roles is None:
            raise AuthenticationFailed("X-User-Role header is required")

        try:
            roles = json.loads(raw_user_roles)
        except json.JSONDecodeError:
            try:
                roles = ast.literal_eval(raw_user_roles)
            except (SyntaxError, ValueError) as exc:
                raise AuthenticationFailed(
                    "X-User-Role header must be a list of strings"
                ) from exc

        if not isinstance(roles, list) or not all(
            isinstance(role, str) for role in roles
        ):
            raise AuthenticationFailed(
                "X-User-Role header must be a list of strings"
            )

        return roles

    def authenticate(self, request):
        raw_user_id = request.META.get(USER_ID_KEY)
        raw_user_roles = request.META.get(USER_ROLE_KEY)

        if not raw_user_id:
            return None

        try:
            user_id = UUID(raw_user_id)
        except (TypeError, ValueError) as exc:
            raise AuthenticationFailed(
                "X-User-Id header must be a valid UUID"
            ) from exc

        user_roles = self._parse_roles(raw_user_roles)

        return (HeaderUser(id=user_id, roles=user_roles), None)
