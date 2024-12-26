# Django Keycloak Authentication Integration

This document provides step-by-step instructions for integrating Keycloak into a Django REST Framework (DRF) project for user authentication and management.

## Features

- **Token Acquisition:** Obtain access tokens from Keycloak using the authorization code flow.
- **Token Verification:** Verify token validity using Keycloak's public key.
- **Automatic User Management:** Create or update Django users based on information retrieved from the token.
- **Protected Views:** Secure API endpoints using DRF permission classes for authorized users only.
- **Error Handling:** Handle expired or invalid tokens gracefully.
- **Keycloak Synchronization (Optional):** Synchronize user data between Keycloak and your Django database.
- **DRF Compatibility:** Seamlessly integrates with DRF's permission system.

## Prerequisites

1. Install Docker.
2. Install Django and Django REST Framework in your Python environment.
3. Basic familiarity with Django, DRF, and Keycloak.

## Keycloak Setup

1. **Start Keycloak in Development Mode:**

   ```bash
   docker run -p 8080:8080 -e KC_BOOTSTRAP_ADMIN_USERNAME=admin -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:26.0.7 start-dev
   ```

2. **Create a Realm:**
   - Log in to the Keycloak admin console at `http://127.0.0.1:8080` using the admin credentials.
   - Click **Add Realm** and provide a name for the realm (e.g., `django`).

3. **Create a User:**
   - Navigate to the **Users** section under the created realm.
   - Click **Add User** and provide user details.
   - Set a password for the user in the **Credentials** tab and enable the `Temporary` toggle.

4. **Create Clients:**

   - **Public Client:**
     - Navigate to **Clients** and click **Create**.
     - Set the client type to `public` and provide a name (e.g., `public-client`).
     - Enable **Direct Access Grants** in the client settings.

   - **Private Client:**
     - Create another client and set the type to `confidential`.
     - Provide a client secret (used for server-to-server communication).

## Django Integration

### 1. Install Required Libraries

Install the following libraries in your Django project:

```bash
pip install django djangorestframework PyJWT python-keycloak
```

### 2. Configure Keycloak in Django

Add the following settings to your `settings.py`:

```python
KEYCLOAK_CONFIG = {
    "SERVER_URL": "http://127.0.0.1:8080/",
    "REALM_NAME": "django",
    "PUBLIC_CLIENT_ID": "public-client",
    "CONFIDENTIAL_CLIENT_ID": "private-client",
}
```

### 3. Create a Custom Authentication Class

Refer to the `KeycloakAuthentication` class provided earlier in this document. This class verifies tokens, retrieves user data, and automatically creates or updates Django users.

### 4. Update DRF Settings

Set the default authentication class in your `settings.py`:

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "path.to.KeycloakAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
```

### 5. Add Protected Views

Create a simple protected view in your Django app:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated!"})
```

### 6. Define URLs

Add the following to your `urls.py`:

```python
from django.urls import path
from .views import ProtectedView

urlpatterns = [
    path('api/protected/', ProtectedView.as_view(), name='protected'),
]
```

## Testing the Integration

### 1. Acquire an Access Token

Send a POST request to the Keycloak token endpoint:

```bash
curl -X POST http://127.0.0.1:8080/realms/django/protocol/openid-connect/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=public-client" \
  -d "username=<your_username>" \
  -d "password=<your_password>" \
  -d "grant_type=password"
```

You will receive a JSON response containing an access token.
### 2. Login way

- username: The username of the user you want to authenticate with Keycloak.
- password: The password corresponding to the provided username.

```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```
### 3. Access Protected Endpoint

Use the access token to make an authorized request to your protected view:

```bash
curl http://localhost:8000/api/protected/ \
  -H "Authorization: Bearer <your_access_token>"
```

If the token is valid, the server will respond with a success message.

## Optional: Keycloak Synchronization

To synchronize user data between Keycloak and your Django database:

- Use Keycloak's admin API to fetch user details periodically.
- Update Django's user database accordingly.

## Troubleshooting

- **Invalid Token:** Ensure the public key is correctly fetched and configured.
- **Authorization Header Missing:** Verify the client sends the `Authorization` header.
- **Expired Token:** Re-authenticate to acquire a new token.

## Conclusion

This guide demonstrates how to integrate Keycloak for authentication in a Django REST Framework project. Keycloak offers robust authentication and user management capabilities, making it an excellent choice for modern applications.

