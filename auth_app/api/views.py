from rest_framework.generics import CreateAPIView
from .serializers import RegistrationSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken

class RegistrationView(CreateAPIView):
    """
    API endpoint for registering a new user.
    Validates the incoming data, creates the user, and generates an auth token.
    Returns the token along with basic user information.
    """
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to register a new user.
        - Validates the input data
        - Creates the user instance
        - Generates or retrieves the auth token
        - Returns token, username, email, and user ID
        """
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, create = Token.objects.get_or_create(user=user)

        response = {
            "token": token.key,
            "username": user.username,
            "email": user.email,
            "user_id": user.pk
        }

        return Response(response, status=status.HTTP_201_CREATED)
    

class LoginView(ObtainAuthToken):
    """
    API endpoint for logging in an existing user.
    Validates credentials and returns an authentication token on success.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to authenticate a user.
        - Validates login credentials using LoginSerializer
        - Authenticates the user
        - Generates or retrieves the auth token
        - Returns token, username, email, and user ID
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, create = Token.objects.get_or_create(user=user)

        response = {
            "token": token.key,
            "username": user.username,
            "email": user.email,
            "user_id": user.pk
        }

        return Response(response, status=status.HTTP_200_OK)