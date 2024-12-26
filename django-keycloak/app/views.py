import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from environs import Env

env = Env()
env.read_env()


class LoginView(APIView):
    def post(self, request) -> Response:
        username = request.data.get("username")
        password = request.data.get("password")

        # Keycloak token endpoint
        token_url = env.str("TOKEN_URL")

        # Prepare the data for token request
        data = {
            "client_id": "public-client",
            "grant_type": "password",
            "username": username,
            "password": password,
        }

        try:
            # Get tokens from Keycloak
            response = requests.post(token_url, data=data)
            response.raise_for_status()

            tokens = response.json()
            return Response(
                {
                    "access_token": tokens["access_token"],
                    "refresh_token": tokens["refresh_token"],
                    "expires_in": tokens["expires_in"],
                }
            )

        except requests.exceptions.RequestException as e:
            return Response(
                data={"error": "Authentication failed", "details": str(e)}, status=400
            )


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request) -> Response:
        return Response(
            data={
                "message": "You have accessed a protected endpoint",
                "user": request.user.username,
            },
            status=200,
        )
