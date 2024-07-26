from rest_framework import permissions

class GeneroPermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genero.view_genero')
        
        if request.method == 'POST':
            return request.user.has_perm('genero.add_genero')
        
        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('genero.change_genero')
        
        if request.method == 'DELETE':
            return request.user.has_perm('genero.delete_genero')

        return False