import jwt
from django.contrib.auth.models import User
from keycloak import KeycloakOpenID
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from environs import Env

env = Env()
env.read_env()


class KeycloakAuthentication(BaseAuthentication):
    def __init__(self):
        # Initialize Keycloak client
        self.keycloak = KeycloakOpenID(
            server_url=env.str("SERVER_URL"),
            realm_name=env.str("REALM_NAME"),
            client_id=env.str("PUBLIC_CLIENT_ID"),
        )
        # Fetch and store the public key for token verification
        try:
            self.public_key = (
                "-----BEGIN PUBLIC KEY-----\n"
                + self.keycloak.public_key()
                + "\n-----END PUBLIC KEY-----"
            )
        except Exception as e:
            self.public_key = None
            print(f"Error fetching public key: {e}")

    def authenticate(self, request):
        # Retrieve the Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None

        try:
            # Split the header to extract the token
            token_type, token = auth_header.split()
            if token_type.lower() != "bearer":
                raise AuthenticationFailed("Invalid token type. Expected 'Bearer'.")

            if not self.public_key:
                raise AuthenticationFailed(
                    "Public key not available for token verification."
                )

            # Decode and verify the token
            options = {
                "verify_signature": True,
                "verify_exp": True,
                "verify_aud": False,  # Adjust based on your Keycloak configuration
            }

            decoded_token = jwt.decode(
                token,
                self.public_key,
                algorithms=["RS256"],  # Keycloak uses RS256 for signing tokens
                options=options,
            )

            # Extract user information from the token
            username = decoded_token.get("preferred_username")
            email = decoded_token.get("email", "")

            if not username:
                raise AuthenticationFailed(
                    "Token does not contain 'preferred_username'."
                )

            # Get or create the user in Django
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": email,
                    "first_name": decoded_token.get("given_name", ""),
                    "last_name": decoded_token.get("family_name", ""),
                },
            )

            return (user, None)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired.")
        except jwt.InvalidTokenError as e:
            raise AuthenticationFailed(f"Invalid token: {str(e)}")
        except ValueError:
            raise AuthenticationFailed("Invalid Authorization header format.")
        except Exception as e:
            raise AuthenticationFailed(f"Authentication failed: {str(e)}")
