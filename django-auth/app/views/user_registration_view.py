from typing import Any

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import CustomTokenObtainPairSerializer, UserRegistrationSerializer


class UserRegistrationView(APIView):
    def __init__(self, **kwargs: Any) -> None:
        self.token_serializer = CustomTokenObtainPairSerializer()
        super().__init__(**kwargs)

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = self.token_serializer.get_token(user)
            access_token = str(token.access_token)
            refresh_token = str(token)
            return Response(
                data={
                    "user": {
                        "username": user.username,
                        "email": user.email,
                        "is_active": user.is_active,
                        "is_staff": user.is_staff,
                        "is_admin": user.is_admin,
                        "created_at": user.created_at,
                        "updated_at": user.updated_at,
                    },
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "message": "Successfully registered a new user!",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data={"errors": serializer.error_messages},
            status=status.HTTP_400_BAD_REQUEST,
        )
