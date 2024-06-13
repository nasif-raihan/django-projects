from rest_framework import serializers


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={"style_input": "password"}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={"style_input": "password"}, write_only=True)

    class Meta:
        fields = ["password", "password2"]

        