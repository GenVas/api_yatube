from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):

        return (True if request.method in permissions.SAFE_METHODS
                or obj.author == request.user else False)
