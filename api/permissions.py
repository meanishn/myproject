from rest_framework import permissions

class IsOwnerAndSuperVisorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user and obj.is_supervisor
        
class IsEmployerOrSupervisor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_employer or request.user.employee.is_supervisor
            
