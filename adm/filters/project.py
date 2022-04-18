from django_filters import rest_framework as filters

from adm.models import Project


class ProjectListFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__title', lookup_expr='iexact', label='Название категории')
    university = filters.CharFilter(field_name='university__title', lookup_expr='iexact', label='Название университета')
    title = filters.CharFilter(lookup_expr='icontains', label="Название проекта")

    class Meta:
        model = Project
        fields = (
            'category',
            'university',
            'title',
        )
