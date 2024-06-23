from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from environs import Env
from rest_framework import serializers

from ..models import User

env = Env()
env.read_env()


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
        link = f"http://localhost:3000/api/user/reset-password/{user_id}/{token}"
        print(f"Reset password {link=}")
        data = {
            "subject": "Reset your password",
            "body": f"Please click the following link to reset your password: {link}",
            "to_email": user.email,
        }
        self.send_mail(data)
        return attrs

    @staticmethod
    def send_mail(data: dict) -> bool:
        email = EmailMessage(
            subject=data.get("subject"),
            body=data.get("body"),
            from_email=env.str("EMAIL_FROM"),
            to=[data.get("to_email")],
        )
        return email.send()
