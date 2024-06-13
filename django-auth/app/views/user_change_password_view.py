from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserChangePasswordSerializer


class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                data={"message": "Successfully changed the user's password."},
                status=status.HTTP_201_CREATED,
            )
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
