from rest_framework import permissions


class LoginAndViewPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
    }
    authenticated_users_only = True
