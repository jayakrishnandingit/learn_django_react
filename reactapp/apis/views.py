from django.contrib.auth import get_user_model

from rest_framework import (
    views as drf_views, generics as drf_generic_views,
    permissions as drf_permissions
)

from reactapp.apis.serializers import UserSerializer
from reactapp.apis.permissions import LoginAndViewPermissions

User = get_user_model()


class UserListAPIView(drf_generic_views.ListAPIView):
    model = User
    # http://www.django-rest-framework.org/api-guide/permissions/#using-with-views-that-do-not-include-a-queryset-attribute
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = None

    ordering = ('first_name',)
    # fields that can be sorted.
    ordering_fields = ('first_name', 'last_name', 'date_joined')

    permission_classes = []
