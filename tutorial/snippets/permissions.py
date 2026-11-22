from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение для разрешения только владельцам объекта
    редактировать его.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение разрешены для любого запроса,
        # поэтому мы всегда разрешаем запросы GET, HEAD или OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешения на запись доступны только владельцу сниппета.
        return obj.owner == request.user