from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserPasswordResetSerializer


class UserPasswordResetView(APIView):
    def post(self, request, user_id, token):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={"user_id": user_id, "token": token}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            data={"message": "Password reset successfully"}, status=status.HTTP_200_OK
        )
