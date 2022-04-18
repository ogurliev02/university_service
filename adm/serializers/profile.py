from rest_framework import serializers

from adm.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Profile
        fields = (
            'user',
            'first_name',
            'last_name',
            'username',
            'group_number',
            'university',
        )
        depth = 1
