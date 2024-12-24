from rest_framework import serializers

from ..models import User


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ["username", "password"]
