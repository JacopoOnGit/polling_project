from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio']
        extra_kwargs = {
            'password': {'write_only': True},
            'bio': {'required': False}
        }

    def create(self, validated_data):
        validated_data.pop('is_staff', None)
        validated_data.pop('is_superuser', None)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

