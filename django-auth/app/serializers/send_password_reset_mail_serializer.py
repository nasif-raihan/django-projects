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
        user = User.objects.filter(email=email)

        if user is None:
            raise serializers.ValidationError("You are not a registered user.")

        uid = urlsafe_base64_encode(s=force_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)
        link = f"http://localhost:3000/api/user/reset/{uid}/{token}"
        body = f"Click Following Link to Reset Your Password: {link}"
        data = {
            "subject": "Reset your password",
            "body": body,
            "to_mail": user.email,
        }
        return attrs
