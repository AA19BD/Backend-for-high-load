import sys
import os
sys.path.append(os.getcwd())
from rest_framework.permissions import IsAuthenticated
from utils.constants import USER_ROLE_CLIENT


class ClientPermission(IsAuthenticated):
    message = 'You are not client'

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_CLIENT


class ClientOrAdminPermission(IsAuthenticated):
    message = 'You are not client or admin'

    def has_permission(self, request, view):
        return super().has_permission(request, view) and (request.user.role == USER_ROLE_CLIENT or request.user.is_superuser)



