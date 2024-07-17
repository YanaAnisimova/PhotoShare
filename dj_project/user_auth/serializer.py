from django.contrib.auth.models import Group
from django.utils.text import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from group import Groups
from user_auth.models import User


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.HiddenField(default=Group.objects.get(name=Groups.SIMPLE_USER.value))

    class Meta:
        model = User
        fields = ['url', 'id', 'first_name', 'last_name', 'username', 'password', 'groups', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


