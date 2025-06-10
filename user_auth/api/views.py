from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_auth.api.serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from user_auth.models import User


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({
            'token': token.key,
            'fullname': user.fullname,
            'email': user.email,
            'id': user.id
        }, status=status.HTTP_201_CREATED)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'fullname': user.fullname,
                    'email': user.email,
                    'user_id': user.id,
                }, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Invalid password"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except User.DoesNotExist:
            return Response(
                {"error": "Email not found"},
                status=status.HTTP_400_BAD_REQUEST
            )
