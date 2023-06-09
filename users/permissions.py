from rest_framework.permissions import BasePermission, SAFE_METHODS, DjangoObjectPermissions, IsAdminUser


class IsAdminUserOrReadOnly(BasePermission):
    """
    Allows access only to admin users or readonly.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        user = request.user

        if hasattr(obj, 'user') and obj.owner == user:
            return True

        return False


class CustomDjangoObjectPermissions(DjangoObjectPermissions):
    perms_map = {
        # 'GET': ['%(app_label)s.view_%(model_name)s', '%(app_label)s.see_premium_%(model_name)s', ],
        'GET': ['%(app_label)s.see_premium_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class IsPremiumUser(BasePermission):
    pass

    def has_permission(self, request, view):
        return request.user.has_perm('see_premium_product')


class IsOwnerorReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user
