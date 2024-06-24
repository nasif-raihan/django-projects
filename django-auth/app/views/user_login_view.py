from typing import Any

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import CustomTokenObtainPairSerializer, UserLoginSerializer


class UserLoginView(APIView):
    def __init__(self, **kwargs: Any) -> None:
        self.token_serializer = CustomTokenObtainPairSerializer()
        super().__init__(**kwargs)

    def post(self, request) -> Response:
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            user = authenticate(username=username, password=password)
            if user is None:
                return Response(
                    data={"errors": "username or password is not matched!"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

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
                    "message": "User logged in successfully",
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            data={"message": serializer.error_message},
            status=status.HTTP_400_BAD_REQUEST,
        )
