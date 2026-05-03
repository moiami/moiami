from rest_framework.permissions import BasePermission

from api.common.authentication import HeaderUser


class IsAdminHeaderUser(BasePermission):
    message = 'Admin role is required'

    def has_permission(self, request, view):
        user = request.user

        return isinstance(user, HeaderUser) and 'admin' in user.roles
