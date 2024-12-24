from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import User


class RefreshTokenView(APIView):
    @staticmethod
    def post(request) -> Response:
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                data={"message": "Valid refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(token=refresh_token)

            user = User.objects.get(id=token["user_id"])
            access_token = str(token.access_token)

            return Response(
                data={
                    "user": {
                        "username": user.username,
                        "email": user.email,
                        "is_admin": user.is_admin,
                        "created_at": user.created_at,
                    },
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "message": "Successfully refreshed the auth token!",
                },
                status=status.HTTP_200_OK,
            )

        except (InvalidToken, TokenError):
            return Response(
                data={"message": "Valid refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except User.DoesNotExist:
            return Response(
                data={"message": "User does not exist!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
