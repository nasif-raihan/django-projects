from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers

from ..models import User


class SendPasswordResetMailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ["email"]

    def validate(self, attrs):
        email = attrs.get("email")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("You are not a registered user.")

        user_id = urlsafe_base64_encode(s=force_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)
        link = f"http://localhost:3000/api/user/reset/{user_id}/{token}"
        body = f"Please click the following link to reset your password: {link}"
        data = {
            "subject": "Reset your password",
            "body": body,
            "to_mail": user.email,
        }
        return attrs
