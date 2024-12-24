from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserChangePasswordSerializer


class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request) -> Response:
        serializer = UserChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={"message": "Successfully changed the user's password."},
            status=status.HTTP_201_CREATED,
        )
