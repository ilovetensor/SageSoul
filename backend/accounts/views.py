from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class RegistrationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        email = request.data.get('email')

        if password1 != password2:
            return Response({"error":"Both passwords do not match."}, status = status.HTTP_400_BAD_REQUEST)

        if not username or not password1:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username is already taken."}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email = email):
            return Response({"error": "The email address is already registered"}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        user = User.objects.create_user(username=username, password=password1, email=email)

        # Generate tokens for the newly registered user
        refresh = RefreshToken.for_user(user)
        tokens = {"refresh": str(refresh), "access": str(refresh.access_token)}

        return Response(tokens, status=status.HTTP_201_CREATED)
