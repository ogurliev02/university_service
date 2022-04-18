from django_filters import rest_framework as filters

from adm.models import Profile


class ProfileListFilter(filters.FilterSet):
    username = filters.CharFilter(field_name='user__username', lookup_expr='iexact', label='Имя пользователя')

    class Meta:
        model = Profile
        fields = (
            'username',
        )
