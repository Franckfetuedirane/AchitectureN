# hospital/api/permissions.py
from rest_framework.permissions import BasePermission

class IsAdminOrDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.groups.filter(name='Doctors').exists()

class IsNurseOrAbove(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_staff or 
                request.user.groups.filter(name='Doctors').exists() or 
                request.user.groups.filter(name='Nurses').exists())