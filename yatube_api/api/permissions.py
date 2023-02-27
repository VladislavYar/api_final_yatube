from rest_framework.permissions import BasePermission, SAFE_METHODS
from api.exceptions import (
    PermissionNotAuthorChangeDenied, PermissionDenied,
    PermissionAddChangeDenied)


class UpdateDestroyPermission(BasePermission):
    """Проверка разрешения на изменение/удаление."""
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif not request.user.is_authenticated:
            raise PermissionDenied()
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif not obj.author == request.user:
            raise PermissionNotAuthorChangeDenied()
        return True


class ReadOnlyPermission(BasePermission):
    """Разрешает только чтение."""
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        raise PermissionAddChangeDenied()


class FollowPermission(BasePermission):
    """Проверка разрешения на подпись автора."""
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied()
        return True

    def has_object_permission(self, request, view, obj):
        if not obj.user == request.user:
            raise PermissionNotAuthorChangeDenied()
        return True
