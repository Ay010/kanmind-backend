from rest_framework import serializers
from user_auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname', 'email']
        read_only_fields = ['id', 'fullname', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['fullname', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self, **kwargs):
        if self.validated_data['password'] != self.validated_data['repeated_password']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        user = User.objects.create_user(
            fullname=self.validated_data['fullname'],
            email=self.validated_data['email'],
            password=self.validated_data['password']
        )
        return user
