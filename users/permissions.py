from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    """
    Пермишен для суперюзера
    """
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsOwner(BasePermission):
    """
    Пермишен для пользователя, создавшего объект
    """
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
