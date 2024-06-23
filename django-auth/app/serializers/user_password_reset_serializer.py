from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers

from ..models import User


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        fields = ["password", "password2"]

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        user_id = self.context.get("user_id")
        token = self.context.get("token")

        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password did not match!"
            )

        try:
            user_id = urlsafe_base64_decode(user_id).decode()
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("Token is not valid or expired!")

            user.set_password(password)
            user.save()
            return attrs

        except (DjangoUnicodeDecodeError, User.DoesNotExist) as e:
            raise serializers.ValidationError("Token is not valid or expired!")
