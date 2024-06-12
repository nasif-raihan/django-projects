from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
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
                    "message": "Successfully registered a new user!",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data={"message": serializer.error_messages},
            status=status.HTTP_400_BAD_REQUEST,
        )
