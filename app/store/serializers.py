from accounts.serializers import DeveloperSerializer
from rest_framework import serializers
from store.models import *


class BriefApplicationSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'name', 'description', 'developer', 'cover',
                  'file', 'is_active', 'created_at', 'updated_at']


class ApplicationSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'name', 'description', 'developer', 'cover',
                  'file', 'created_at', 'updated_at']

    def create(self, user):
        return Application.objects.create(
            developer=user,
            **self.validated_data
        )
