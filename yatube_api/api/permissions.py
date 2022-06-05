from rest_framework import permissions


class IsAutherOrReadOnly(permissions.BasePermission):
    message = "У вас недостаточно прав для выполнения данного действия!"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author
