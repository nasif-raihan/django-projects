from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import SendPasswordResetMailSerializer


class SendPasswordResetMailView(APIView):
    def post(self, request):
        serializer = SendPasswordResetMailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            data={"message": "Password reset link has been sent!"},
            status=status.HTTP_200_OK,
        )
