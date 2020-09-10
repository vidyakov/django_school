from rest_framework import serializers

from .models import SchoolUser


class SchoolUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolUser
        fields = 'email', 'first_name', 'last_name', 'password'
        extra_kwargs = {'password': {'write_only': True}}
