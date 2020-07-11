from rest_framework import serializers
from .models import Students


class StudentsSerializer(serializers.Serializer):
    FirstName = serializers.CharField(max_length=50)
    LastName = serializers.CharField(max_length=50)
    Email = serializers.CharField()
    Password = serializers.CharField()

    def create(self, validated_data):
        return Students.objects.create(**validated_data)
