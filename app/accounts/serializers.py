from rest_framework import serializers
from accounts.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'phone', 'is_developer', 'image',
                  'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        u = User(**validated_data)
        u.set_password(validated_data['password'])
        u.save()
        return u


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['image', 'first_name', 'last_name',]
