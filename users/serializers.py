from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'role',
        )

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class UserListSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'role',
        )

    def get_id(self, obj) -> int:
        return obj.pk


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )