from django_filters import rest_framework as filters
from rest_framework import permissions
from rest_framework.generics import ListAPIView

from adm.filters.profile import ProfileListFilter
from adm.models import Profile
from adm.serializers.profile import ProfileSerializer


class ProfileListView(ListAPIView):
    queryset = Profile.objects.select_related('user').order_by('user_id')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ProfileSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProfileListFilter
