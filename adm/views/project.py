from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView
from rest_framework import permissions

from adm.models import Project
from adm.filters.project import ProjectListFilter
from adm.serializers.project import ProjectSerializer


class ProjectListView(ListAPIView):
    queryset = Project.objects.select_related('project_manager')
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProjectListFilter
