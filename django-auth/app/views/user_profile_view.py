from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserProfileSerializer


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # print(f"{request.header=}")
        print(f"{request.user=}")
        serializer = UserProfileSerializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        # return Response(
        #     data=serializer.error_messages, status=status.HTTP_400_BAD_REQUEST
        # )
