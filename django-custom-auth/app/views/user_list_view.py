from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import User
from ..serializers import UserProfileSerializer


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request) -> Response:
        users = User.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
