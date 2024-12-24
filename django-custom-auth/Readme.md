# Django Authentication API

This project is a Django-based authentication system utilizing JWT for securing the endpoints. It includes several REST API endpoints to manage user authentication and profile operations.

## Overview

This API allows users to:
- Register a new account
- Log in to an existing account
- Change their password
- Retrieve their profile information
- Retrieve all user information (admin)
- Send a password reset email
- Reset their password
- Refresh authentication tokens

## Endpoints

### 1. Register

**URL:** `/api/user/register/`

**Method:** `POST`

**Body:**
```json
{
    "password": "password",
    "password2": "password",
    "email": "email@example.com",
    "username": "username"
}
```

### 2. Login

**URL:** `/api/user/login/`

**Method:** `POST`

**Body:**
```json
{
    "username": "username",
    "password": "password"
}
```

### 3. Change Password

**URL:** `/api/user/change-password/`

**Method:** `POST`

**Authorization:** Bearer Token

**Body:**
```json
{
    "password": "newpassword",
    "password2": "newpassword"
}
```

### 4. Profile

**URL:** `/api/user/profile/`

**Method:** `GET`

**Authorization:** Bearer Token

### 5. Get All Users

**URL:** `/api/user/all`

**Method:** `GET`

**Authorization:** Bearer Token

### 6. Send Reset Password Email

**URL:** `/api/user/reset-password-email/`

**Method:** `POST`

**Body:**
```json
{
    "email": "email@example.com"
}
```

### 7. Reset Password

**URL:** `/api/user/reset-password/{uid}/{token}/`

**Method:** `POST`

**Body:**
```json
{
    "password": "newpassword",
    "password2": "newpassword"
}
```

### 8. Refresh Auth Token

**URL:** `/api/user/token/refresh/`

**Method:** `POST`

**Body:**
```json
{
    "refresh": "refresh_token"
}
```

## Usage

To use this API, you need to:
1. Set up the Django project and configure the JWT settings.
2. Use a tool like Postman to test the endpoints.
3. Include the `Authorization` header with the Bearer token for protected endpoints.

## Configuration

Ensure you have set the `{{host}}` variable in your Postman collection or environment to point to your API server.

## Contributing

If you wish to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.