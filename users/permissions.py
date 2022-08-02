from rest_framework import permissions


class IsLibrarian(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.role == 1:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True